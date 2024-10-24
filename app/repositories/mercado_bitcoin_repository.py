import httpx
from urllib.parse import urljoin
from datetime import datetime
from app.common.cache_decorator import redis_cache
from app.models.coin_models import CoinRequest, CoinResponse, Variation
from app.core.interfaces.base_crypto_repository import BaseCryptoRepository

class MercadoBitcoinRepository(BaseCryptoRepository):
    BASE_URL = "https://store.mercadobitcoin.com.br/"

    @redis_cache(cache_key_prefix="mercado-bitcoin-get_coin_info")
    def get_coin_info(self, request: CoinRequest) -> CoinResponse:
        params = {
            "symbol": request.symbol.lower(),
            "limit": 1,
            "offset": 0,
            "order": "desc",
            "sort": "release_date"
        }

        response = httpx.get(url=urljoin(self.BASE_URL, "api/v1/marketplace/product/unlogged"), params=params)
        response.raise_for_status()
        
        data = response.json()

        product = data["response_data"]["products"][0]

        icon_url = product["icon_url"]["png"]
        coin_price_brl = float(product["market_price"])
        coin_price_usd = coin_price_brl / 5.0

        return CoinResponse(
            total_items=data["total_items"],
            coin_name=product["name"],
            product_id=product["product_id"],
            name=product["name"],
            icon_url={
                "svg": product["icon_url"]["svg"],
                "png": icon_url
            },
            type=product["type"],
            market_price=str(coin_price_brl),
            description=product["description"],
            symbol=product["product_data"]["symbol"],
            variation=Variation(
                string=f"{product['product_data']['variation']['string']}",
                number=product['product_data']['variation']['number'],
                status=product['product_data']['variation']['status']
            ),
            market_cap=product["product_data"]["market_cap"],
            release_date=product["product_data"]["release_date"],
            quote="BRL",
            coin_price=coin_price_brl,
            coin_price_dolar=f"{coin_price_usd:.6f}",
            date_consult=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ).model_dump()
