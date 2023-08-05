from typing import TYPE_CHECKING, Any

from .rdp_stream import RDPStream
from ..._tools import try_copy_to_list

if TYPE_CHECKING:
    from ..._types import ExtendedParams, StrStrings
    from ..._core.session import Session


class Definition:
    """
    This class to subscribe to streaming items of RDP streaming protocol
    that exposed by the underlying of the Refinitiv Data

    Parameters
    ----------
    service: string, optional
        name of RDP service
    universe: list
        RIC to retrieve item stream.
    view: list
        data fields to retrieve item stream
    parameters: dict
        extra parameters to retrieve item stream.
    api: string
        specific name of RDP streaming defined
        in config file. i.e. 'streaming.trading-analytics.endpoints.redi'
    extended_params: dict, optional
        Specify optional params
        Default: None

    Examples
    --------
    >>> from refinitiv.data.delivery import rdp_stream
    >>> definition = rdp_stream.Definition(
    ...     service=None,
    ...     universe=[],
    ...     view=None,
    ...     parameters={"universeType": "RIC"},
    ...     api="streaming.trading-analytics.endpoints.redi",
    ...)
    """

    def __init__(
        self,
        service: str,
        universe: Any,
        view: "StrStrings",
        parameters: dict,
        api: str,
        extended_params: "ExtendedParams" = None,
    ) -> None:
        self._service = service
        if not isinstance(universe, dict):
            universe = try_copy_to_list(universe)
        self._universe = universe
        self._view = try_copy_to_list(view)
        self._parameters = parameters
        self._api = api
        self._extended_params = extended_params

    def get_stream(self, session: "Session" = None) -> RDPStream:
        stream = RDPStream(
            session=session,
            service=self._service,
            universe=self._universe,
            view=self._view,
            parameters=self._parameters,
            api=self._api,
            extended_params=self._extended_params,
        )
        return stream
