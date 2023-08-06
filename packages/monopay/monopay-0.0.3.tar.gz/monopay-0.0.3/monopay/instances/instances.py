__all__ = [
    'QrListItem',
    'WalletItem',
    'CancelListItem',
    'MerchantStatementItem'
]

from typing import Optional, List
from dataclasses import dataclass


@dataclass
class QrListItem:
    short_qr_id: str
    qr_id: str
    amount_type: str
    page_url: str


@dataclass
class CanceledItem:
    pass


@dataclass
class CancelListItem:
    amount: int
    ccy: int
    date: str
    approval_code: Optional[str]
    rrn: Optional[str]
    masked_pan: str


@dataclass
class MerchantStatementItem:
    invoice_id: str
    status: str
    masked_pan: str
    date: str
    payment_scheme: str
    amount: int
    profit_amount: Optional[int]
    ccy: int
    approval_code: Optional[str]
    rrn: Optional[str]
    reference: Optional[str]
    short_qr_id: Optional[str]
    cancel_list: List[CancelListItem]


@dataclass
class WalletItem:
    card_token: str
    masked_pan: str
    country: Optional[str] = None
