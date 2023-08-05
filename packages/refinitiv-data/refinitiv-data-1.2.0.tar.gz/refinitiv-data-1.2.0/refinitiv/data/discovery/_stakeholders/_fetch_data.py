from typing import Tuple, List

import pandas as pd
from pandas import DataFrame

from ._relationship_type import RelationshipType
from ._stakeholder_data import Customer, Supplier, StakeholderData
from ...content import fundamental_and_reference, symbol_conversion
from ...delivery._data._response import Response

data_class_by_relationship_type = {
    RelationshipType.CUSTOMER: Customer,
    RelationshipType.SUPPLIER: Supplier,
}

FIELDS = [
    "TR.SCRelationship",
    "TR.SCRelationship.ScorgIDOut",
    "TR.SCRelationship.instrument",
    "TR.SCRelationshipConfidenceScore",
    "TR.SCRelationshipFreshnessScore",
    "TR.SCRelationshipUpdateDate",
]

TO_SYMBOL_TYPES = [
    symbol_conversion.SymbolTypes.RIC,
    symbol_conversion.SymbolTypes.ISIN,
    symbol_conversion.SymbolTypes.CUSIP,
    symbol_conversion.SymbolTypes.SEDOL,
]


def get_fundamental_data(instrument) -> Response:
    response = fundamental_and_reference.Definition(universe=instrument, fields=FIELDS).get_data()
    return response


def get_symbol_conversion_data(ric_list) -> Response:
    response = symbol_conversion.Definition(
        symbols=ric_list,
        from_symbol_type=symbol_conversion.SymbolTypes.OA_PERM_ID,
        to_symbol_types=TO_SYMBOL_TYPES,
    ).get_data()
    return response


def merge_dataframes(fundamental_df, symbol_conversion_df) -> pd.DataFrame:
    # symbol_conversion df index to 'Related OrganizationID' column
    symbol_conversion_df.reset_index(inplace=True)
    symbol_conversion_df = symbol_conversion_df.rename(columns={"index": "Related OrganizationID"})

    # Merge by Related OrganizationID column
    return pd.merge(fundamental_df, symbol_conversion_df, how="outer", on="Related OrganizationID")


def fetch_data(instrument: str, relationship_type: RelationshipType) -> Tuple[List[StakeholderData], DataFrame]:
    fund_response = get_fundamental_data(instrument)
    fund_data = [i for i in fund_response.data.raw.get("data", []) if i[1] == relationship_type.value]
    # fund_data -> [["VOD.L", "Customer", "5000051106", "VOD.L", 0.29598408, 1, "2018-06-08"], ...]
    ric_list = [i[2] for i in fund_data]
    # ric_list -> ["5000051106", ...]
    symbol_response = get_symbol_conversion_data(ric_list)

    symbol_data = symbol_response.data.raw.get("Matches")
    # symbol_data -> {"5000051106": {"DocumentTitle": "Indian", "RIC": "IOTL.NS"}, ...}

    retval = []
    for stakeholder_data in fund_data:
        stakeholder = data_class_by_relationship_type[relationship_type].from_list(stakeholder_data)

        stakeholder_symbol_data = symbol_data.get(stakeholder.related_organization_id)
        if stakeholder_symbol_data:
            stakeholder.update(stakeholder_symbol_data)

        retval.append(stakeholder)

    fundamental_df = fund_response.data.df
    # drop lines where wrong relationship_type
    fundamental_df = fundamental_df.drop(
        fundamental_df[fundamental_df["Relationship Type"] != relationship_type.value].index
    )
    return retval, merge_dataframes(fundamental_df, symbol_response.data.df)
