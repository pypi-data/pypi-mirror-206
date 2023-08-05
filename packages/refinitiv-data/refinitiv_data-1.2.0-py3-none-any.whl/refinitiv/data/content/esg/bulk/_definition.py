from typing import TYPE_CHECKING

from ._db_manager import (
    create_db_manager_by_package_name,
    DBManager,
)
from ...._tools import try_copy_to_list
from ...._tools._common import fields_arg_parser, universe_arg_parser

if TYPE_CHECKING:
    from ...._types import StrStrings, OptStrStrs


class Response:
    pass


class Definition:
    """
    This class describe parameters to retrieve ESG data.

    Parameters
    ----------
    package_name : str

    universe : str, list of str
        The Universe parameter allows the user to define the company they
        want content returned for, ESG content is delivered at the Company Level.

    fields : list, optional
        The list of fields that are to be returned in the response

    Examples
    --------
    >>> import refinitiv.data.content.esg.bulk as bulk
    >>> definition = bulk.Definition(
    ...     package_name='standard_scores',
    ...     universe=['4295875817', '4295889298'],
    ...     fields=["instrument", "periodenddate"]
    ... )
    >>> response = definition.get_db_data()
    >>> df = response.data.df
    >>> print(df)

    """

    def __init__(
        self,
        package_name: str,
        universe: "StrStrings",
        fields: "OptStrStrs" = None,
    ) -> None:
        fields = try_copy_to_list(fields)
        self._fields = fields and fields_arg_parser.get_list(fields)
        universe = try_copy_to_list(universe)
        self._universe = universe_arg_parser.get_list(universe)
        self._db_manager: DBManager = create_db_manager_by_package_name(package_name)

    def get_db_data(self) -> Response:
        """
        Returns a response to the data platform

        Returns
        -------
        Response

        """
        data = self._db_manager.get_data(universe=self._universe, fields=self._fields)
        response = Response()
        response.data = data
        return response
