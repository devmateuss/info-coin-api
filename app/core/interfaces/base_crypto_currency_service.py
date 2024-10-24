

from abc import ABC
from app.models.crypto_currency_model import ProductRequest, ProductResponse


class BaseCryptoCurrencyService(ABC):

    def get_products(self, request: ProductRequest) -> ProductResponse:
        """
        Fetches products from the external cryptocurrency API.
        :param request: ProductRequest containing filters like symbol, limit, offset, etc.
        :return: ProductResponse with the fetched data.
        """
        raise NotImplementedError()