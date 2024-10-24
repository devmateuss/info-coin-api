from abc import ABC, abstractmethod
from app.models.crypto_currency_model import ProductRequest, ProductResponse

class BaseCryptoCurrencyRepository(ABC):
    """
    Interface for CryptoCurrency service.
    """

    @abstractmethod
    def fetch_products(self, request: ProductRequest) -> ProductResponse:
        """
        Fetches products from the external cryptocurrency API.
        :param request: ProductRequest containing filters like symbol, limit, offset, etc.
        :return: ProductResponse with the fetched data.
        """
        raise NotImplementedError()
