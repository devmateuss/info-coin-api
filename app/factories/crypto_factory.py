from app.repositories.mercado_bitcoin_repository import MercadoBitcoinRepository
from app.repositories.coingecko_repository import CoinGeckoRepository
from app.core.interfaces.base_crypto_repository import BaseCryptoRepository

class CryptoFactory:
    @staticmethod
    def create(provider: str) -> BaseCryptoRepository:
        if provider == "mercadobitcoin":
            return MercadoBitcoinRepository()
        elif provider == "coingecko":
            return CoinGeckoRepository()
        else:
            raise ValueError("Invalid provider specified")
