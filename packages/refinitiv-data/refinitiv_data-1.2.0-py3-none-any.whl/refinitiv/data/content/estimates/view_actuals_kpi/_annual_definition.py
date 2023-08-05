from typing import TYPE_CHECKING

from ..._content_data import Data
from ..._content_provider_layer import ContentUsageLoggerMixin
from ...._content_type import ContentType
from ...._tools import validate_bool_value, try_copy_to_list
from ....delivery._data._data_provider import DataProviderLayer, BaseResponse

if TYPE_CHECKING:
    from ...._types import StrStrings, ExtendedParams


class Definition(
    ContentUsageLoggerMixin[BaseResponse[Data]],
    DataProviderLayer[BaseResponse[Data]],
):
    """
    This class describe parameters to retrieves estimates actuals values for KPI Measures for reported annual periods.

    Parameters
    ----------
    universe: str, list of str
        The Universe parameter allows the user to define the companies for which the content is returned.

    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    extended_params: ExtendedParams, optional
        If necessary other parameters.

    Examples
    --------
    >>> from refinitiv.data.content import estimates
    >>> definition = estimates.view_actuals_kpi.annual.Definition(universe="BNPP.PA")
    >>> response = definition.get_data()
    """

    _USAGE_CLS_NAME = "Estimates.ActualsKPI.AnnualDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)

        super().__init__(
            ContentType.ESTIMATES_VIEW_ACTUALS_KPI_ANNUAL,
            universe=universe,
            use_field_names_in_headers=use_field_names_in_headers,
            extended_params=extended_params,
        )
