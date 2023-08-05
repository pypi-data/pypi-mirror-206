from datetime import timedelta, datetime
from typing import Union, Optional

from ._tools import _convert_date_time
from .._data._data_provider_layer import DataProviderLayer
from .._data._data_type import DataType
from ..._tools import validate_types


class Definition(DataProviderLayer):
    """
    Definition object.

    Parameters
    __________
        fileset_id : str
            The name of the file-set for files to be searched.
            Only exactly matched results are returned.
        file_name : str, optional
            Filter results by file name.
        created_since : str or timedelta or datetime, optional
            Filter results by when the Bucket was created.
        modified_since : str or timedelta or datetime, optional
            Filter results by when the Bucket was last modified.
        skip_token : str, optional
            Used for server-side paging.
        page_size : int, optional
            Used for server-side paging.
            By default 25.

    Methods
    -------
    get_data(session=session)
        Returns a response to the data platform
    get_data_async(session=None)
        Returns a response asynchronously to the data platform

    Examples
    --------
    >>> from refinitiv.data.delivery import cfs
    >>> definition = cfs.files.Definition()
    >>> files = definition.get_data()

    Using get_data_async

    >>> import asyncio
    >>> task = definition.get_data_async()
    >>> response = asyncio.run(task)
    """

    def __init__(
        self,
        fileset_id: str,
        file_name: Optional[str] = None,
        created_since: Union[str, datetime, timedelta] = None,
        modified_since: Union[str, datetime, timedelta] = None,
        skip_token: Optional[str] = None,
        page_size: int = 25,
    ):
        validate_types(page_size, [int, type(None)], "page_size")
        created_since = _convert_date_time(created_since)
        modified_since = _convert_date_time(modified_since)
        super().__init__(
            data_type=DataType.CFS_FILES,
            fileset_id=fileset_id,
            file_name=file_name,
            created_since=created_since,
            modified_since=modified_since,
            skip_token=skip_token,
            page_size=page_size,
        )
