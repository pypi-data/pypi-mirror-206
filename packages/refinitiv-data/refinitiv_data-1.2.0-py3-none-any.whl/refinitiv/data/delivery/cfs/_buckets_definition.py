from typing import TYPE_CHECKING, Optional

from ._tools import _convert_date_time
from .._data._data_provider_layer import DataProviderLayer
from .._data._data_type import DataType
from ..._tools import validate_types, attributes_arg_parser, try_copy_to_list

if TYPE_CHECKING:
    from ..._types import OptStrStrs


class Definition(DataProviderLayer):
    """
    Definition object.

    Parameters
    __________
        name : str, optional
            Filter results by Bucket name. (Partial match).
        created_since : str, optional
            Filter results by when the Bucket was created.
            The date/time format is YYYY-MM-DDTHH:mm:ssZ.(e.g. 2020-01-21T04:19:01Z).
        modified_since : str, optional
            Filter results by when the Bucket was last modified.
            The date/time format is YYYY-MM-DDTHH:mm:ssZ.(e.g. 2020-01-21T04:19:01Z).
        available_from : str, optional
            Filter results by when the Bucket was made available.
            The date/time format is YYYY-MM-DDTHH:mm:ssZ.(e.g. 2020-01-21T04:19:01Z).
        available_to : str, optional
            Filter results by when the Bucket was made available.
            The date/time format is YYYY-MM-DDTHH:mm:ssZ.(e.g. 2020-01-21T04:19:01Z).
        attributes : list of str, optional
            List of publisher-defined bucket attributes.
        page_size : int, optional
            Number of buckets returned.
            By default 25.
        skip_token : str, optional
            Skip token is only used if a previous operation returned a partial result.
            If a previous response contains a nextLink element, the value of the nextLink
            element will include a skip token parameter that specifies a starting point to use
            for subsequent calls.

    Methods
    -------
    get_data(session=session)
        Returns a response to the data platform
    get_data_async(session=None)
        Returns a response asynchronously to the data platform

    Examples
    --------
    >>> from refinitiv.data.delivery import cfs
    >>> definition = cfs.buckets.Definition()
    >>> buckets = definition.get_data()

    Using get_data_async

    >>> import asyncio
    >>> task = definition.get_data_async()
    >>> response = asyncio.run(task)
    """

    def __init__(
        self,
        name: Optional[str] = None,
        created_since: Optional[str] = None,
        modified_since: Optional[str] = None,
        available_from: Optional[str] = None,
        available_to: Optional[str] = None,
        attributes: "OptStrStrs" = None,
        page_size: int = 25,
        skip_token: Optional[str] = None,
    ):
        validate_types(page_size, [int], "page_size")
        created_since = _convert_date_time(created_since)
        modified_since = _convert_date_time(modified_since)
        available_from = _convert_date_time(available_from)
        available_to = _convert_date_time(available_to)
        if attributes:
            attributes = try_copy_to_list(attributes)
            attributes = attributes_arg_parser.get_list(attributes)
            attributes = ";".join(attributes)
        super().__init__(
            data_type=DataType.CFS_BUCKETS,
            name=name,
            created_since=created_since,
            modified_since=modified_since,
            available_from=available_from,
            available_to=available_to,
            attributes=attributes,
            page_size=page_size,
            skip_token=skip_token,
        )
