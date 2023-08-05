from electricalclientv4.paths.history_id_.get import ApiForget
from electricalclientv4.paths.history_id_.put import ApiForput
from electricalclientv4.paths.history_id_.delete import ApiFordelete
from electricalclientv4.paths.history_id_.patch import ApiForpatch


class HistoryId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
