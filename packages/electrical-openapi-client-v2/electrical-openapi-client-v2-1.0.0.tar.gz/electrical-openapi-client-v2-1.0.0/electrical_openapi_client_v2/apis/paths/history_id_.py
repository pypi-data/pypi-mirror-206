from electrical_openapi_client_v2.paths.history_id_.get import ApiForget
from electrical_openapi_client_v2.paths.history_id_.put import ApiForput
from electrical_openapi_client_v2.paths.history_id_.delete import ApiFordelete
from electrical_openapi_client_v2.paths.history_id_.patch import ApiForpatch


class HistoryId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
