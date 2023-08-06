from .base_exception import MonoPayBaseException


class InvalidatedToken(MonoPayBaseException):
    errCode = "FORBIDDEN"
    errText = "invalid 'X-Token'"
