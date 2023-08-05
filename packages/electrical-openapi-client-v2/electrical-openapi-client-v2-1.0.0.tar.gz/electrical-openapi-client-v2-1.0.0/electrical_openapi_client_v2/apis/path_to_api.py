import typing_extensions

from electrical_openapi_client_v2.paths import PathValues
from electrical_openapi_client_v2.apis.paths.history_ import History
from electrical_openapi_client_v2.apis.paths.history_id_ import HistoryId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HISTORY_: History,
        PathValues.HISTORY_ID_: HistoryId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HISTORY_: History,
        PathValues.HISTORY_ID_: HistoryId,
    }
)
