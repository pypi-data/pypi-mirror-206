# coding: utf8


from typing import TYPE_CHECKING, Optional

from .omm_stream import OMMStream
from ..._tools import create_repr, fields_arg_parser, try_copy_to_list

if TYPE_CHECKING:
    from ..._types import ExtendedParams, OptStrStrs
    from ..._core.session import Session


class Definition:
    """
    This class to subscribe to streaming items of any Domain Model
    (e.g. MarkePrice, MarketByPrice, ...)
    exposed by the underlying of the Refinitiv Data

    Parameters
    ----------
    name : str, optional
        Name of the streaming instrument
    api: str, optional
        Specifies the data source. It can be updated/added using config file
    service : str, optional
        Offers the ability to use specific service to manage the
        real-time streaming data
    fields : str or list, optional
        Specifies the specific fields delivered when messages arrive
    domain : str, optional
        Defines the domain for the specific data of interest
        Default : "MarketPrice"
    extended_params : dict, optional
        Other parameters can be provided if necessary

    Examples
    --------
    >>> from refinitiv.data.delivery import omm_stream
    >>> definition = omm_stream.Definition("EUR")
    """

    def __init__(
        self,
        name: str,
        api: Optional[str] = None,
        service: Optional[str] = None,
        fields: "OptStrStrs" = None,
        domain: str = "MarketPrice",
        extended_params: "ExtendedParams" = None,
    ) -> None:
        self._name = name
        self._api = api
        self._domain = domain
        self._service = service
        fields = try_copy_to_list(fields)
        self._fields = fields and fields_arg_parser.get_list(fields)
        self._extended_params = extended_params

    def __repr__(self):
        content = f"{{name='{self._name}'}}"
        return create_repr(self, middle_path="omm_stream", content=content)

    def get_stream(self, session: "Session" = None) -> OMMStream:
        """
        Initialization subscribe to streaming items

        Parameters
        ----------
        session: Session, optional
            The Session defines the source where you want to retrieve your data

        Returns
        -------
        current instance

        Examples
        --------
        >>> from refinitiv.data.delivery import omm_stream
        >>> definition = omm_stream.Definition("EUR")
        >>> stream = definition.get_stream()
        """
        stream = OMMStream(
            session=session,
            name=self._name,
            api=self._api,
            service=self._service,
            fields=self._fields,
            domain=self._domain,
            extended_params=self._extended_params,
        )
        return stream
