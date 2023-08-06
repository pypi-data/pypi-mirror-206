from typing import Optional, List, Any
from ..resource import Resource


def list(
    source: Optional[Any] = None,
    *,
    name: Optional[str] = None,
    type: Optional[str] = None,
    **options,
) -> List[Resource]:
    """List resources

    Parameters:
        source: a data source
        type: data type
        **options: Resource options

    Returns:
        data resources
    """

    # Create resource
    resource = (
        source
        if isinstance(source, Resource)
        else Resource(source, datatype=type, **options)
    )

    # List resource
    return resource.list(name=name)
