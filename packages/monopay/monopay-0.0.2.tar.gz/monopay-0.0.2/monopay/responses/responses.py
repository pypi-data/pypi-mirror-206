__all__ = [
    'InvoiceCreatedResponse',
    'InvoiceCanceledResponse',
    'InvoiceStatusResponse',
    'InvoiceInfoResponse',
    'SplitInvoiceResponse',
    'FinalizeInvoiceResponse',
    'QrListResponse',
    'QrDetailsResponse',
    'MerchantDetailsResponse',
    'MerchantStatementResponse',
    'MerchantPubKeyResponse',
    'WalletCardsResponse',
    'EmptyResponse'
]

from typing import Optional, List
from dataclasses import dataclass
from ..instances import QrListItem, MerchantStatementItem, WalletItem


@dataclass
class EmptyResponse:
    pass


@dataclass
class InvoiceCreatedResponse:
    invoice_id: str
    page_url: str


@dataclass
class InvoiceCanceledResponse:
    status: str
    created_date: str
    modified_date: str


@dataclass
class SplitInvoiceResponse:
    reference: str


@dataclass
class InvoiceStatusResponse:
    pass


@dataclass
class InvoiceInfoResponse:
    pass


@dataclass
class FinalizeInvoiceResponse:
    status: str


@dataclass
class QrListResponse:
    list: List[QrListItem]


@dataclass
class QrDetailsResponse:
    short_qr_id: str
    invoice_id: Optional[str]
    amount: Optional[int]
    ccy: Optional[int]


@dataclass
class MerchantDetailsResponse:
    merchant_id: str
    merchant_name: str


@dataclass
class MerchantStatementResponse:
    list: List[MerchantStatementItem]


@dataclass
class MerchantPubKeyResponse:
    key: str


@dataclass
class WalletCardsResponse:
    wallets: List[WalletItem]
