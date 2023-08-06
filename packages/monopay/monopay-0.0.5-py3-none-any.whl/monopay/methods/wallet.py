from typing import Union
from ..exceptions import MonoPayBaseException
from ..responses import EmptyResponse, WalletCardsResponse
from ..instances import WalletItem
from ..utils import is_exception
import requests


class Wallet:
    def __init__(
        self,
        base_url: str,
        headers
    ):
        self.base_url = base_url
        self.headers = headers

        self.cards_list_url = f"{self.base_url}/api/merchant/wallet"
        self.card_payment_url = f"{self.base_url}/api/merchant/wallet/payment"
        self.delete_card_url = f"{self.base_url}/api/merchant/wallet/card"

    def cards(self, wallet_id: str):
        params = {
            "walletId": wallet_id,
        }

        response = requests.get(
            url=self.cards_list_url,
            headers=self.headers,
            params=params
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return WalletCardsResponse(
            wallets=[
                WalletItem(
                    card_token=item['cardToken'],
                    masked_pan=item['maskedPan'],
                    country=item['country']
                ) for item in response_data['wallets']
            ]
        )

    def payment(self):
        pass

    def delete_card(self, card_token: str) -> Union[EmptyResponse, MonoPayBaseException]:
        params = {
            "cardToken": card_token,
        }

        response = requests.delete(
            url=self.cards_list_url,
            headers=self.headers,
            params=params
        )

        response_data = response.json()

        if is_exception(response):
            return MonoPayBaseException(
                err_code=response_data['errCode'],
                err_text=response_data['errText']
            )

        return EmptyResponse()
