import typing_extensions

from electrical_openapi_client_v2.apis.tags import TagValues
from electrical_openapi_client_v2.apis.tags.history_api import HistoryApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.HISTORY: HistoryApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.HISTORY: HistoryApi,
    }
)
