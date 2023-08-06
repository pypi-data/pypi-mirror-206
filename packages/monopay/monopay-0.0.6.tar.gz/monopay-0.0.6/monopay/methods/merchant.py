from typing import Union, Optional
from monopay.responses import MerchantDetailsResponse, MerchantStatementResponse, MerchantPubKeyResponse
from monopay.utils import is_exception
from monopay.exceptions import MonoPayBaseException
from monopay.instances import MerchantStatementItem, CancelListItem
from monopay.decorators import request
import requests


class Merchant:
    def __init__(self, base_url: str, headers):
        self.base_url = base_url
        self.headers = headers

        self.merchant_details_url = f"{self.base_url}/api/merchant/details"
        self.merchant_statement_url = f"{self.base_url}/api/merchant/statement"
        self.merchant_pubkey_url = f"{self.base_url}/api/merchant/pubkey"

    @request(url='merchant_details_url')
    def details(self, response_data) -> Union[MerchantDetailsResponse, MonoPayBaseException]:

        return MerchantDetailsResponse(
            merchant_id=response_data['merchantId'],
            merchant_name=response_data['merchantName'],
        )

    @request('merchant_statement_url')
    def statement(
        self,
        from_timestamp: int,
        to_timestamp: Optional[int] = None,
        response_data=None,
    ) -> Union[MerchantStatementResponse, MonoPayBaseException]:

        return MerchantStatementResponse(
            list=[
                MerchantStatementItem(
                    invoice_id=statement_item['invoiceId'],
                    status=statement_item['status'],
                    masked_pan=statement_item['maskedPan'],
                    date=statement_item['date'],
                    payment_scheme=statement_item['paymentScheme'],
                    amount=statement_item['amount'],
                    profit_amount=statement_item['profitAmount'],
                    ccy=statement_item['ccy'],
                    approval_code=statement_item['approvalCode'],
                    rrn=statement_item['rrn'],
                    reference=statement_item['reference'],
                    short_qr_id=statement_item['shortQrId'],
                    cancel_list=[
                        CancelListItem(
                            amount=cancel_item['amount'],
                            ccy=cancel_item['ccy'],
                            date=cancel_item['date'],
                            approval_code=cancel_item['approvalCode'],
                            rrn=cancel_item['rrn'],
                            masked_pan=cancel_item['maskedPan']
                        ) for cancel_item in statement_item['cancelList']
                    ]
                ) for statement_item in response_data['list']
            ]
        )

    @request(url='merchant_pubkey_url')
    def pubkey(self, response_data) -> Union[MerchantPubKeyResponse, MonoPayBaseException]:

        return MerchantPubKeyResponse(
            key=response_data['key']
        )
