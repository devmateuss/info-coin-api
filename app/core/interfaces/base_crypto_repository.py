# src/core/interfaces/base_crypto_api.py
from abc import ABC, abstractmethod
from app.models.coin_models import CoinRequest, CoinResponse

class BaseCryptoRepository(ABC):
    @abstractmethod
    def get_coin_info(self, request: CoinRequest) -> CoinResponse:
        """
        Fetches information about a given cryptocurrency symbol.
        """
        raise NotImplementedError   
