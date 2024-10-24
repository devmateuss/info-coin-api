from app.common.cache_decorator import redis_cache
from app.core.interfaces.base_crypto_currency_service import BaseCryptoCurrencyService
from app.models.crypto_currency_model import ProductRequest, ProductResponse
from app.repositories.crypto_currency_bitcoin_market_repository import CryptoCurrencyRepository


class CryptoCurrencyService(BaseCryptoCurrencyService):
    """
    Service to handle business logic for interacting with cryptocurrency products.
    """

    def __init__(self):
        self.repository = CryptoCurrencyRepository()

    @redis_cache(cache_key_prefix="get_products")
    def get_products(self, request: ProductRequest) -> ProductResponse:
        """
        Fetches products from the external cryptocurrency API.
        :param request: ProductRequest containing filters like symbol, limit, offset, etc.
        :return: ProductResponse with the fetched data.
        """
        return self.repository.fetch_products(request)
