from rest_framework import request as rf_request

from trench.backends.base import AbstractMessageDispatcher
from trench.models import MFAMethod
from trench.query.get_mfa_config_by_name import get_mfa_config_by_name_query
from trench.settings import HANDLER


def get_mfa_handler(
    mfa_method: MFAMethod, request: rf_request.Request | None = None
) -> AbstractMessageDispatcher:
    conf = get_mfa_config_by_name_query(name=mfa_method.name)
    dispatcher = conf[HANDLER]
    return dispatcher(mfa_method=mfa_method, config=conf, request=request)
