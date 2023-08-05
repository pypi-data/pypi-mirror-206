from typing import Union, TYPE_CHECKING

from ..._content_data import Data
from ..._content_provider_layer import ContentUsageLoggerMixin
from .._enums import Package
from ...._content_type import ContentType
from ...._tools import validate_types, validate_bool_value, try_copy_to_list
from ....delivery._data._data_provider import DataProviderLayer, BaseResponse

if TYPE_CHECKING:
    from ...._types import StrStrings, ExtendedParams


class Definition(
    ContentUsageLoggerMixin[BaseResponse[Data]],
    DataProviderLayer[BaseResponse[Data]],
):
    """
    This class describe parameters to retrieves estimates actuals values for reported annual periods.

    Parameters
    ----------
    universe: str, list of str
        The Universe parameter allows the user to define the companies for which the content is returned.

    package: str, Package
        Packages of the content that are subsets in terms of breadth (number of fields) and depth (amount of history) of
        the overall content set. Types of packages: basic, standard, professional

    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    extended_params: ExtendedParams, optional
        If necessary other parameters.

    Examples
    --------
    >>> from refinitiv.data.content import estimates
    >>> definition = estimates.view_actuals.annual.Definition(
    ...     universe="IBM.N",
    ...     package=estimates.Package.BASIC
    ... )
    >>> response = definition.get_data()
    """

    _USAGE_CLS_NAME = "Estimates.Actuals.AnnualDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        package: Union[str, Package],
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        validate_types(package, [str, Package], "package")
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)

        super().__init__(
            ContentType.ESTIMATES_VIEW_ACTUALS_ANNUAL,
            universe=universe,
            package=package,
            use_field_names_in_headers=use_field_names_in_headers,
            extended_params=extended_params,
        )
