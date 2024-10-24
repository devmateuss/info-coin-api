from app.common.cache_decorator import redis_cache
from app.factories.crypto_factory import CryptoFactory
from app.models.coin_models import CoinRequest, CoinResponse


class CoinService:

    @redis_cache(cache_key_prefix="get_coin_info")
    def get_coin_info(self, request: CoinRequest, provider: str) -> CoinResponse:
        """
        Gets coin information using the specified provider.
        :param request: CoinRequest with the symbol of the cryptocurrency.
        :param provider: The provider name (e.g., 'mercadobitcoin', 'coingecko').
        :return: CoinResponse with the fetched data.
        """
        repository = CryptoFactory.create(provider)
        return repository.get_coin_info(request)