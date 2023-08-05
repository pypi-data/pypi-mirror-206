import typing_extensions

from electricalclientv4.paths import PathValues
from electricalclientv4.apis.paths.history_ import History
from electricalclientv4.apis.paths.history_id_ import HistoryId

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
