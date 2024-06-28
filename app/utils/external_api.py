import requests
from fastapi.exceptions import HTTPException

from ..core.config import settings
from ..api.schemas.currency import CurrencyConvert


class CurrencyAPI:
    def __init__(self):
        self.EXTERNAL_API_URL = 'https://api.apilayer.com/currency_data'
        self.headers = {"apikey": settings.EXTERNAL_API_KEY}

    def get_convert(
            self,
            query_params: CurrencyConvert
    ) -> int | HTTPException:
        response = requests.get(
            f'{self.EXTERNAL_API_URL}/convert',
            params={
                'to': query_params.to_currency,
                'from': query_params.from_currency,
                'amount': query_params.amount,
            },
            headers=self.headers
        )

        if response.status_code == 200:
            return response.json()['result']
        else:
            raise HTTPException(status_code=400, detail='Bad currency code')

    def get_list(self) -> dict[str, str] | None:
        response = requests.get(
            f'{self.EXTERNAL_API_URL}/list',
            headers=self.headers
        )

        if response.status_code == 200:
            return response.json()['currencies']
        return None
