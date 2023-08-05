import collections
from dataclasses import dataclass, field
from enum import Enum, unique
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ._response import Response

Error = collections.namedtuple("Error", ["code", "message"])


@unique
class RequestMethod(str, Enum):
    """
    The RESTful Data service can support multiple methods when
    sending requests to a specified endpoint.
       GET : Request data from the specified endpoint.
       POST : Send data to the specified endpoint to create/update a resource.
       DELETE : Request to delete a resource from a specified endpoint.
       PUT : Send data to the specified endpoint to create/update a resource.
    """

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class EndpointData:
    raw: Any
    _owner: "Response" = None
    _kwargs: Dict = field(default_factory=dict)
