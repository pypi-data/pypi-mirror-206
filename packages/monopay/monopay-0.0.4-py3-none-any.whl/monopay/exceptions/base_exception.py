from dataclasses import dataclass


@dataclass
class MonoPayBaseException:
    err_code: str
    err_text: str
