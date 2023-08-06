from typing import Union
from ..responses import QrDetailsResponse, QrListResponse, EmptyResponse
from ..exceptions import MonoPayBaseException
from ..instances import QrListItem
from ..utils import is_exception
from ..decorators import request, post_request
import requests


class Qr:
    def __init__(
        self,
        base_url: str,
        headers
    ):
        self.base_url = base_url
        self.headers = headers

        self.qr_list_url = f"{self.base_url}/api/merchant/qr/list"
        self.qr_details_url = f"{self.base_url}/api/merchant/qr/details"
        self.qr_reset_amount_url = f"{self.base_url}/api/merchant/qr/reset-amount"

    @request(url='qr_list_url')
    def list(self, response_data) -> Union[QrListResponse, MonoPayBaseException]:

        items = [
            QrListItem(
                short_qr_id=item['shortQrId'],
                qr_id=item['qrId'],
                amount_type=item['amountType'],
                page_url=item['pageUrl']
            ) for item in response_data['list']
        ]

        return QrListResponse(
            list=items
        )

    @request(url='qr_details_url')
    def details(
        self,
        qr_id: str,
        response_data
    ) -> Union[QrDetailsResponse, MonoPayBaseException]:

        return QrDetailsResponse(
            short_qr_id=response_data['shortQrId'],
            invoice_id=response_data['invoiceId'] if "invoiceId" in response_data else None,
            amount=response_data['amount'] if "amount" in response_data else None,
            ccy=response_data['ccy'] if "ccy" in response_data else None,
        )

    @post_request(url='qr_reset_amount_url')
    def reset_amount(
        self,
        qr_id: str,
        response_data
    ) -> Union[EmptyResponse, MonoPayBaseException]:

        return EmptyResponse()

