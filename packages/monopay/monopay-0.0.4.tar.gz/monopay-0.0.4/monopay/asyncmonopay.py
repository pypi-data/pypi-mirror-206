from .methods import Merchant, Invoice, Qr, Wallet


class AsyncMonoPay:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.monobank.ua"
        self.headers = {
            "X-Token": self.api_token
        }
        self.merchant: Merchant = Merchant(
            base_url=self.base_url,
            headers=self.headers
        )
        self.invoice: Invoice = Invoice(
            base_url=self.base_url,
            headers=self.headers
        )
        self.qr: Qr = Qr(
            base_url=self.base_url,
            headers=self.headers
        )
        self.wallet: Wallet = Wallet(
            base_url=self.base_url,
            headers=self.headers
        )

    def set_api_token(self, api_token) -> None:
        self.api_token = api_token

    def get_api_token(self) -> str:
        return self.api_token
