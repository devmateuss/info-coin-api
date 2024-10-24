import httpx
from datetime import datetime
from app.models.coin_models import CoinRequest, CoinResponse, Variation
from app.core.interfaces.base_crypto_repository import BaseCryptoRepository
from app.common.coins_type import CoinsType

class CoinGeckoRepository(BaseCryptoRepository):
    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_coin_info(self, request: CoinRequest) -> CoinResponse:
        coin_name = CoinsType.get_name(request.symbol)

        market_response = httpx.get(
            f"{self.BASE_URL}/coins/markets",
            params={
                "vs_currency": "brl",
                "ids": coin_name
            }
        )
        market_response.raise_for_status()
        market_data = market_response.json()[0]

        detail_response = httpx.get(f"{self.BASE_URL}/coins/{coin_name}")
        detail_response.raise_for_status()
        detail_data = detail_response.json()

        icon_url = detail_data["image"]["large"]
        description = detail_data["description"]["en"]

        coin_price_brl = market_data.get("current_price", 0)
        coin_price_usd = detail_data["market_data"]["current_price"].get("usd", 0)

        return CoinResponse(
            total_items=1,
            coin_name=market_data["name"],
            product_id=request.symbol.upper(),
            name=market_data["name"],
            icon_url={
                "svg": icon_url,
                "png": icon_url
            },
            type="crypto",
            market_price=str(coin_price_brl),
            description=description,
            symbol=market_data["symbol"].upper(),
            variation=Variation(
                string=f"{market_data.get('price_change_percentage_24h', 0):.2f}%",
                number=market_data.get('price_change_percentage_24h', 0),
                status="positive" if market_data.get('price_change_percentage_24h', 0) > 0 else "negative"
            ),
            market_cap=str(market_data.get("market_cap", 0)),
            release_date=detail_data.get("genesis_date", "N/A"),
            quote="BRL",
            coin_price=coin_price_brl,
            coin_price_dolar=f"{coin_price_usd:.6f}",
            date_consult=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )