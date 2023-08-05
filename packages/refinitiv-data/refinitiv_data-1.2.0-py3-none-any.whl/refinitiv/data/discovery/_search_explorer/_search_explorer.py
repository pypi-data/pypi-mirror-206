from typing import Union

import pandas as pd
import numpy as np

from refinitiv.data.content import search
from refinitiv.data.content.search import Views

from refinitiv.data.discovery._search_explorer._dataclasses import (
    SearchPropertyExplorerResponse,
    from_list,
)


class SearchPropertyExplorer:
    """
    SearchPropertyExplorer object provides ability to get search data and metadata.
    Transform results, merge responses from two requests.
    """

    def __init__(self):
        self._navigator = None
        self._query = None
        self._filter = None
        self._view = None
        self._order_by = None
        self._navigators = None
        self._navigator = None

    def get_properties_for(
        self,
        query: str = None,
        filter: str = None,
        view: Union[Views, str] = Views.SEARCH_ALL,
        order_by: str = None,
        navigators: str = None,
    ) -> SearchPropertyExplorerResponse:
        """
        Retrieve search data and metadata. Transform results, create
        properties and navigators objects, merge responses into single object.

        Parameters
        ----------
        query: str, optional
            Keyword argument for view

        view: Views or str, optional
            The view for searching see at Views enum.
            Default: Views.SEARCH_ALL

        filter: str, optional
            Where query is for unstructured end-user-oriented restriction, filter is for
            structured programmatic restriction.

        order_by: str, optional
            Defines the order in which matching documents should be returned.

        navigators: str, optional
            This can name one or more properties, separated by commas, each of which must
            be Navigable.

        Returns
        -------
            SearchPropertyExplorerResponse

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> response = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))"
        ...)
        """
        self._query = query
        self._filter = filter
        self._view = view
        self._order_by = order_by
        self._navigators = navigators
        self._navigator = None

        # Retrieve metadata and prepare column details
        meta = search.metadata.Definition(view=view).get_data()
        # Search and process debug output
        search_df = self._search_and_extract(query, filter, view, order_by, navigators)

        metadata_df = self._filter_metadata_df(meta, search_df)
        df = self._merge_dfs(metadata_df, search_df)
        properties = self._create_properties(df)

        return SearchPropertyExplorerResponse(
            hits_count=self._hits_count,
            properties=properties,
            df=df,
            metadata=metadata_df,
            navigators=self._navigator,
        )

    @staticmethod
    def _filter_metadata_df(metadata, search_df):
        data_for_metadata_df = []
        metadata_properties = metadata.data.raw["Properties"]

        for prop in metadata_properties:
            if prop in search_df["Property"].values:
                metadata_properties[prop]["Property"] = prop
                data_for_metadata_df.append(metadata_properties[prop])

        metadata = pd.DataFrame(data_for_metadata_df)
        metadata.set_index("Property", inplace=True)
        metadata.replace(np.nan, False, inplace=True)
        return metadata

    @staticmethod
    def _merge_dfs(metadata_df: pd.DataFrame, search_df: pd.DataFrame) -> pd.DataFrame:
        if metadata_df.index.nlevels > 1:
            metadata_df.index.set_names(["Property", "Nested"], inplace=True)
            metadata_df.reset_index(inplace=True)
            metadata_df.loc[(metadata_df.Property == metadata_df.Nested), "Nested"] = ""
            _df = search_df.join(metadata_df.set_index(["Property"]), on=["Property"])
            _df.drop("Nested", inplace=True, axis=1)
        else:
            metadata_df.index.set_names(["Property"], inplace=True)
            metadata_df.reset_index(inplace=True)
            _df = search_df.join(metadata_df.set_index(["Property"]), on="Property")
        _df.replace({np.nan: pd.NA}, inplace=True)
        _df = _df.astype("str")
        return _df

    def _create_properties(self, df: pd.DataFrame) -> dict:
        properties = df.values.tolist()

        request_arguments = {
            "query": self._query,
            "filter": self._filter,
            "view": self._view,
            "order_by": self._order_by,
            "navigators": self._navigators,
        }

        property_dict = {_property[0]: from_list(_property, request_arguments) for _property in properties}

        return property_dict

    def _search_and_extract(
        self,
        query: str,
        filter: str,
        view: Union[Views, str],
        order_by: str,
        navigators: str,
    ) -> pd.DataFrame:
        filtered_data = []

        response = search.Definition(
            view=view,
            query=query,
            filter=filter,
            top=1,
            select="_debugall",
            order_by=order_by,
            navigators=navigators,
        ).get_data()

        self._hits_count = response.total
        self._extract_navigator(response)

        if response.total > 0:
            filtered_data = self._parse_search_response(response.data.raw["Hits"][0]["raw_source"])
        return pd.DataFrame(filtered_data, columns=["Property", "Example Value"])

    def _extract_navigator(self, response):
        counts_flag = False
        data = {}
        buckets_counts = []
        dfs = []
        if "Navigators" not in response.data.raw:
            return

        navigators = list(response.data.raw["Navigators"].items())

        for navigator in navigators:
            for key, bucket in navigator[1].items():
                counts, columns, filters = self._navigator_data(bucket)
                data[navigator[0]] = {navigator[0]: columns, "Count": counts}
                if len(filters) > 0:
                    data[navigator[0]]["Filter"] = filters

                buckets_counts.append(counts)

        if all(item == buckets_counts[0] for item in buckets_counts):
            counts_flag = True

        for navigator, bucket_data in data.items():
            dfs.append(pd.DataFrame(bucket_data))

        if len(dfs) == 1:
            df = dfs[0]
        elif not any(buckets_counts):
            df = pd.DataFrame([], columns=[*data.keys(), "Label", "Count"])
        elif counts_flag:
            df = pd.merge(*dfs, on="Count", how="outer")
        else:
            df = pd.concat(dfs)
            df = df.sort_values("Count", ascending=False)
        df.replace({np.nan: pd.NA}, inplace=True)
        self._navigator = df

    @staticmethod
    def _navigator_data(bucket):
        counts = []
        columns = []
        filters = []

        for value in bucket:
            counts.append(value.get("Count", 0))
            columns.append(value.get("Label", pd.NA))

            if "Filter" in value:
                filters.append(value["Filter"])
        return counts, columns, filters

    @staticmethod
    def _parse_search_response(raw_data: dict) -> list:
        data = []
        unique_prop_names = []

        for _property, value in raw_data.items():
            if isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                for node in value:
                    for nested_property, nested_value in node.items():
                        nested_prop_name = f"{_property}.{nested_property}"
                        if nested_prop_name in unique_prop_names:
                            continue

                        data.append([nested_prop_name, nested_value])
                        unique_prop_names.append(nested_prop_name)
            else:
                if _property in unique_prop_names:
                    continue
                data.append([_property, value])
                unique_prop_names.append(_property)
        return data
