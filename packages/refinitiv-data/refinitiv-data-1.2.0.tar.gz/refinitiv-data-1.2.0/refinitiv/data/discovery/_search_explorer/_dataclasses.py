from dataclasses import dataclass
from enum import IntEnum
from typing import Union
from refinitiv.data.content import search
import pandas as pd


def _convert_property_attribute(value):
    return True if value == "True" else False if value == "False" else pd.NA


def from_list(data: list, request_arguments: dict) -> "Property":
    searchable = _convert_property_attribute(data[3])
    sortable = _convert_property_attribute(data[4])
    navigable = _convert_property_attribute(data[5])
    groupable = _convert_property_attribute(data[6])
    exact = _convert_property_attribute(data[7])
    symbol = _convert_property_attribute(data[8])

    return Property(
        name=data[0],
        value=data[1],
        type=data[2],
        searchable=searchable,
        sortable=sortable,
        navigable=navigable,
        groupable=groupable,
        exact=exact,
        symbol=symbol,
        request_arguments=request_arguments,
    )


class PropertyType(IntEnum):
    Double = 1
    String = 2
    Date = 3
    Boolean = 4
    Integer = 5


@dataclass
class BucketsData:
    """BucketsData has properties for requested navigator."""

    name: str
    value: list
    count: list


@dataclass
class Navigator:
    """Navigator object that has dataframe and BucketsData object for requested navigator."""

    df: pd.DataFrame
    navigator: BucketsData


@dataclass
class Properties:
    """Properties objects that has dataframe and dict object that holds Property objects"""

    df: pd.DataFrame
    properties: dict


@dataclass
class Property:
    """Property object that has data and metadata for specific property."""

    name: str
    value: str
    type: str
    searchable: Union[bool, str]
    sortable: Union[bool, str]
    navigable: Union[bool, str]
    groupable: Union[bool, str]
    exact: Union[bool, str]
    symbol: Union[bool, str]
    request_arguments: dict

    def get_possible_values(self):
        """
        Retrieves the navigator data

        Returns
        -------
            Navigator object

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> result = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> prop = result.properties["RCSIssuerCountry"].get_possible_values()
        """
        response = search.Definition(
            view=self.request_arguments["view"],
            query=self.request_arguments["query"],
            filter=self.request_arguments["filter"],
            top=1,
            select="_debugall",
            order_by=self.request_arguments["order_by"],
            navigators=self.name,
        ).get_data()

        data = {}
        counts = []
        labels = []
        filters = []

        navigator_data = list(response.data.raw["Navigators"].items())
        navigator_name = navigator_data[0][0]
        buckets = navigator_data[0][1]["Buckets"]

        for value in buckets:
            counts.append(value.get("Count", 0))
            labels.append(value.get("Label", pd.NA))

            if "Filter" in value:
                filters.append(value["Filter"])

        data[navigator_name] = labels
        if len(filters) > 0:
            data["Filter"] = filters

        data["Count"] = counts
        navigator_data = BucketsData(name=navigator_name, value=data[navigator_name], count=data["Count"])
        df = pd.DataFrame(data)
        return Navigator(df, navigator_data)


@dataclass
class SearchPropertyExplorerResponse:
    """
    Response object that has stores requested properties data.
    """

    hits_count: int
    properties: dict
    df: pd.DataFrame
    metadata: pd.DataFrame
    navigators: pd.DataFrame

    def get_by_name(self, name: str) -> "Properties":
        """
        Browse the properties that match the specified property name.

        Parameters
        ----------
        name: str
            argument for search in response df and find matched properties.

        Returns
        -------
            Properties

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> prop = properties.get_properties_object("active")
        """

        df = self.get_properties_df(name)
        props = self.get_properties_object(name)
        return Properties(df, props)

    def get_properties_object(self, name: Union[str, bool, int]) -> dict:
        """
        Browse the properties that match the specified property name.

        Parameters
        ----------
        name: Union[str, bool, int]
            argument for search in response df and find matched properties.

        Returns
        -------
            dict of Property objects

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> prop = properties.get_properties_object("active")
        """
        if name is None:
            return self.properties

        return {item: value for item, value in self.properties.items() if str(name).lower() in str(item).lower()}

    def get_properties_df(self, name: str) -> pd.DataFrame:
        """
        Browse the properties that match the specified property name.

        Parameters
        ----------
        name: str
            Item for searching and finding matched properties in response dataframe.

        Returns
        -------
            pd.DataFrame

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> prop = properties.get_properties_df("active")

        """
        return self.df.loc[self.df.Property.str.contains(name.replace(" ", ""), na=False, case=False)]

    def get_by_value(self, value: Union[str, bool, int]) -> Properties:
        """
        Browse the properties that match the specified property value.

        Parameters
        ----------
        value: str, bool, int
            String for searching and finding matched properties in response dataframe.

        Returns
        -------
            Properties

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> prop = properties.get_by_value("active")
        """
        if isinstance(value, bool):
            result = self.get_by_type(PropertyType.Boolean)
            df = result.df
            properties = result.properties
            df = df[df["Example Value"] == str(value)]

            response_properties = {}

            for _property, attributes in properties.items():
                if attributes.value == str(value):
                    response_properties[_property] = attributes
            result = Properties(df, response_properties)

        elif isinstance(value, str) or isinstance(value, int):
            value = str(value)
            props = {
                name: self.properties[name]
                for name, values in self.properties.items()
                if value.lower() in values.value.lower()
            }
            df = self.df.loc[self.df["Example Value"].str.contains(value, na=False, case=False)]

            result = Properties(df, props)
        else:
            raise ValueError("Invalid data type. Please provide number, boolean or string.")
        return result

    def get_navigable(self, prop: str = None) -> "Properties":
        """

        Browse and returns navigable properties.

        Parameters
        ----------
        prop: str
            String to fing the matching types.

        Returns
        -------
            Properties

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> result = properties.get_navigable()
        """
        properties = self.get_properties_object(prop)

        props = {}
        for _property, attributes in properties.items():
            if attributes.navigable is True:
                props[_property] = attributes

        df = self.df.loc[self.df["Navigable"] == "True"]
        if prop:
            df = self._filter_df(df, prop)
        return Properties(df, props)

    def get_by_type(self, property_type: Union[str, PropertyType]) -> Properties:
        """
        Browse the types that match the specified property type

        Parameters
        ----------
        property_type: str, PropertyType
            String to fing the matching types.

        Returns
        -------
            pd.DataFrame

        Examples
        --------
        >>> from refinitiv.data.discovery._search_explorer import SearchPropertyExplorer
        >>> explorer = SearchPropertyExplorer()
        >>> properties = explorer.get_properties_for(
        ...    view=search.Views.GOV_CORP_INSTRUMENTS,
        ...    query = "santander bonds",
        ...    filter = "IsPerpetualSecurity ne true and IsActive eq true and not(AssetStatus in ('MAT' 'DC'))",
        ...)
        >>> result = properties.get_by_type(PropertyType.String)

        """
        if not isinstance(property_type, PropertyType):
            raise ValueError(f"Invalid property type specified. Type must be: {PropertyType}")

        props = {}
        for prop, value in self.properties.items():
            if str(value.type) == property_type.name:
                props[prop] = value

        df = self.df.loc[self.df.Type.str.contains(property_type.name, na=False, case=False)]

        return Properties(df, props)

    @staticmethod
    def _filter_df(df, prop):
        return df.loc[df.Property.str.contains(prop, na=False, case=False)]
