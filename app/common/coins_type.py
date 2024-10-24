class CoinsType:
    """
    Maps common cryptocurrency symbols to their CoinGecko-compatible names.
    """
    SYMBOL_TO_NAME = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "ada": "cardano",
        "dot": "polkadot",
        "xrp": "ripple",
        "ltc": "litecoin",
        "bch": "bitcoin-cash",
        "bnb": "binancecoin",
        "sol": "solana",
        "doge": "dogecoin",
        "matic": "polygon",
        "uni": "uniswap",
        "link": "chainlink",
        "xlm": "stellar",
        "usdt": "tether",
        "usdc": "usd-coin",
        "avax": "avalanche",
        "atom": "cosmos",
        "egld": "elrond",
        "sand": "the-sandbox",
        "mana": "decentraland",
        "algo": "algorand",
        "axs": "axie-infinity",
        "ftm": "fantom",
        "shib": "shiba-inu"
    }

    @classmethod
    def get_name(cls, symbol: str) -> str:
        """
        Converts a symbol to the corresponding CoinGecko name.
        If the symbol is not found, defaults to the symbol itself.
        :param symbol: The symbol of the cryptocurrency (e.g., 'btc').
        :return: The corresponding CoinGecko name (e.g., 'bitcoin').
        """
        return cls.SYMBOL_TO_NAME.get(symbol.lower(), symbol.lower())