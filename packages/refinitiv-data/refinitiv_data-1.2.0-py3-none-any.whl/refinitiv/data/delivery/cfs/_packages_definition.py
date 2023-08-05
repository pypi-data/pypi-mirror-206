from typing import Optional

from .._data._data_provider_layer import DataProviderLayer
from .._data._data_type import DataType
from ..._tools import validate_types


class Definition(DataProviderLayer):
    """
    Definition object.

    Parameters
    __________
        package_name : str, optional
            Filter results by package name. (Partial match).
         package_id: str, optional
            CFS package with package id.
        package_type : str, optional
            Filter results by package type.
            Available values : core, bulk, private.
        bucket_name : str, optional
            List the package that associated with this bucket.
        page : int, optional
            The offest number determine which set of result should be
            returned from all results.
        included_total_result : bool, optional
            The flag to indicate if total record count should be returned.
            By default False.
        skip_token : str, optional
            Skip token is only used if a previous operation returned a partial result.
            If a previous response contains a nextLink element, the value of the nextLink
            element will include a skip token parameter that specifies a starting point to use
            for subsequent calls.
        page_size : int, optional
            The number of package that will be returned into a single response.
            By default 25.
        included_entitlement_result : bool, optional
            The flag to indicate the entitlement checking on each package.
            By default False.

    Methods
    -------
    get_data(session=session)
        Returns a response to the data platform
    get_data_async(session=None)
        Returns a response asynchronously to the data platform

    Examples
    --------
    >>> from refinitiv.data.delivery import cfs
    >>> definition = cfs.packages.Definition()
    >>> packages = definition.get_data()

    Using get_data_async

    >>> import asyncio
    >>> task = definition.get_data_async()
    >>> response = asyncio.run(task)
    """

    def __init__(
        self,
        package_name: Optional[str] = None,
        package_id: Optional[str] = None,
        package_type: Optional[str] = None,
        bucket_name: Optional[str] = None,
        page: Optional[int] = None,
        included_total_result: bool = False,
        skip_token: Optional[str] = None,
        page_size: int = 25,
        included_entitlement_result: bool = False,
    ):
        validate_types(page_size, [int, type(None)], "page_size")
        super().__init__(
            data_type=DataType.CFS_PACKAGES,
            package_name=package_name,
            _package_id=package_id,
            package_type=package_type,
            bucket_name=bucket_name,
            page=page,
            included_total_result=included_total_result,
            skip_token=skip_token,
            page_size=page_size,
            included_entitlement_result=included_entitlement_result,
        )
