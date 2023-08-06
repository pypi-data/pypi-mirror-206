import json
from typing import Union, Optional
from ..utils import is_exception
from ..exceptions import MonoPayBaseException
from ..responses import InvoiceCreatedResponse, SplitInvoiceResponse, InvoiceCanceledResponse, \
    InvoiceStatusResponse, FinalizeInvoiceResponse, EmptyResponse
import requests


class Invoice:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

        self.create_invoice_url = f"{self.base_url}/api/merchant/invoice/create"
        self.split_invoice_url = f"{self.base_url}/api/merchant/invoice/split-payments"
        self.cancel_invoice_url = f"{self.base_url}/api/merchant/invoice/cancel"
        self.invoice_status_url = f"{self.base_url}/api/merchant/invoice/status"
        self.invoice_invalidation_url = f"{self.base_url}/api/merchant/invoice/remove"
        self.invoice_info_url = f"{self.base_url}/api/merchant/invoice/payment-info"
        self.invoice_finalize_url = f"{self.base_url}/api/merchant/invoice/finalize"

    def create(
        self,
        amount: int,
        ccy: Optional[int] = None,
        merchant_payment_info: Optional = None,
        redirect_url: Optional[str] = None,
        web_hook_url: Optional[str] = None,
        validity: Optional[int] = None,
        payment_type: Optional[str] = None,
        qr_id: Optional = None,
        save_card_data: Optional = None,
    ) -> Union[InvoiceCreatedResponse, MonoPayBaseException]:
        data = {
            "amount": amount,
            "ccy": ccy,
            "merchantPaymentInfo": merchant_payment_info,
            "redirectUrl": redirect_url,
            "webHookUrl": web_hook_url,
            "validity": validity,
            "paymentType": payment_type,
            "qrId": qr_id,
            "saveCardData": save_card_data
        }
        response = requests.post(
            url=self.create_invoice_url,
            headers=self.headers,
            data=json.dumps(data),
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return InvoiceCreatedResponse(
            invoice_id=response_data['invoiceId'],
            page_url=response_data['pageUrl']
        )

    def split(self) -> Union[SplitInvoiceResponse, MonoPayBaseException]:
        response = requests.post(
            url=self.split_invoice_url,
            headers=self.headers,
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return SplitInvoiceResponse(
            reference=response_data['reference']
        )

    def cancel(
        self,
        invoice_id: str,
        ext_ref: str,
        amount: int,
        items
    ) -> Union[InvoiceCanceledResponse, MonoPayBaseException]:
        data = {
            "invoiceId": invoice_id,
            "extRef": ext_ref,
            "amount": amount,
            "items": items
        }
        response = requests.post(
            url=self.cancel_invoice_url,
            headers=self.headers,
            data=data
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return InvoiceCanceledResponse(
            status=response_data['status'],
            created_date=response_data['createdDate'],
            modified_date=response_data['modifiedDate']
        )

    def invalidation(
        self,
        invoice_id: str
    ) -> Union[MonoPayBaseException, EmptyResponse]:
        data = {
            "invoiceId": invoice_id
        }
        response = requests.post(
            url=self.invoice_invalidation_url,
            headers=self.headers,
            data=data
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return EmptyResponse()

    def status(
        self,
        invoice_id: str
    ) -> Union[InvoiceStatusResponse, MonoPayBaseException]:

        params = {
            "invoiceId": invoice_id,
        }

        response = requests.get(
            url=self.invoice_status_url,
            headers=self.headers,
            params=params
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return InvoiceStatusResponse()

    def info(
        self,
        invoice_id
    ):
        params = {
            "invoiceId": invoice_id,
        }
        response = requests.get(
            url=self.invoice_info_url,
            headers=self.headers,
            params=params
        )
        return response.json()

    def finalize(
        self,
        invoice_id: str,
        amount: int
    ) -> Union[FinalizeInvoiceResponse, MonoPayBaseException]:
        data = {
            "invoiceId": invoice_id,
            "amount": amount,
        }

        response = requests.post(
            url=self.invoice_finalize_url,
            headers=self.headers,
            data=data
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return FinalizeInvoiceResponse(
            status=response_data['status']
        )

