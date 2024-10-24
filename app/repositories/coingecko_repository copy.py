# src/repositories/coingecko_repository.py

import httpx
from datetime import datetime
from app.models.coin_models import CoinRequest, CoinResponse
from app.core.interfaces.base_crypto_repository import BaseCryptoRepository

class CoinGeckoRepository(BaseCryptoRepository):
    BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    def get_coin_info(self, request: CoinRequest) -> CoinResponse:
        params = {
            "ids": request.symbol.lower(),
            "vs_currencies": "usd,brl"
        }

        response = httpx.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        coin_data = data.get(request.symbol.lower(), {})
        coin_price = coin_data.get("brl", 0)
        coin_price_dolar = f"{coin_data.get('usd', 0):.6f}"

        return CoinResponse(
            coin_name=request.symbol.upper(),
            symbol=request.symbol.upper(),
            coin_price=coin_price,
            coin_price_dolar=coin_price_dolar,
            date_consult=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
