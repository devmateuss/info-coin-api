# src/repositories/crypto_currency_repository.py

import requests
from app.core.interfaces.base_crypto_currency_repository import BaseCryptoCurrencyRepository
from app.models.crypto_currency_model import ProductRequest, ProductResponse

class CryptoCurrencyRepository(BaseCryptoCurrencyRepository):
    """
    Repository to interact with the external cryptocurrency API.
    """

    BASE_URL = "https://store.mercadobitcoin.com.br/api/v1/marketplace/product/unlogged"

    def fetch_products(self, request: ProductRequest) -> ProductResponse:
        """
        Fetches products from the external cryptocurrency API.
        
        :param request: ProductRequest containing filters like symbol, limit, offset, etc.
        :return: ProductResponse with the fetched data.
        """
        params = {
            "symbol": request.symbol,
            "limit": 1,
            "offset": 0,
            "order": "desc",
            "sort": "release_date"
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(self.BASE_URL, params=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        return ProductResponse(**data)