from .._content_data import Data
from ..._content_type import ContentType
from ..._tools import create_repr, validate_bool_value
from ...delivery._data._data_provider import DataProviderLayer, BaseResponse


class Definition(DataProviderLayer[BaseResponse[Data]]):
    """
    This class describe parameters to retrieve data for ESG universe.

    Parameters
    ----------
    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    Examples
    --------
    >>> from refinitiv.data.content import esg
    >>> definition = esg.universe.Definition()
    >>> response = definition.get_data()

    >>> response = await definition.get_data_async()
    """

    def __init__(
        self,
        use_field_names_in_headers: bool = False,
    ):
        validate_bool_value(use_field_names_in_headers)

        super().__init__(
            ContentType.ESG_UNIVERSE,
            use_field_names_in_headers=use_field_names_in_headers,
        )

    def __repr__(self):
        return create_repr(
            self,
            middle_path="universe",
            content=f"{{closure='{self._kwargs.get('closure')}'}}",
        )
