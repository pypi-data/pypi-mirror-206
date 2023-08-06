import datetime

from .methods import Merchant, Invoice, Qr, Wallet


class MonoPay:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.monobank.ua"
        self.headers = {
            "X-Token": self.api_token
        }
        self.merchant = Merchant(
            base_url=self.base_url,
            headers=self.headers
        )
        self.invoice: Invoice = Invoice(
            base_url=self.base_url,
            headers=self.headers
        )
        self.qr = Qr(
            base_url=self.base_url,
            headers=self.headers
        )
        self.wallet = Wallet(
            base_url=self.base_url,
            headers=self.headers
        )

    def set_api_token(self, api_token) -> None:
        self.api_token = api_token

    def get_api_token(self) -> str:
        return self.api_token


# if __name__ == '__main__':
mp = MonoPay(api_token='uAvDe23DVr7MUJpnOTV7rUz_cFyCGlL2bvM74pU05ejc')
res = mp.qr.list()
print(res)
for item in res.list:
    res = mp.qr.details(qr_id=item.qr_id)
    print(res)
    res = mp.qr.reset_amount(qr_id=item.qr_id)
    print(res)

# res = mp.merchant.pubkey()
# print(res)
# res = mp.merchant.details()
# print(res)


