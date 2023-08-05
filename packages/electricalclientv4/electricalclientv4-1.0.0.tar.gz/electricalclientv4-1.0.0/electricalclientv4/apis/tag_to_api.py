import typing_extensions

from electricalclientv4.apis.tags import TagValues
from electricalclientv4.apis.tags.history_api import HistoryApi

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
