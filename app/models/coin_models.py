from pydantic import BaseModel, Field
from typing import Optional, Dict

class CoinRequest(BaseModel):
    """
    Model to validate the input for a coin information request.
    """
    symbol: str = Field(..., example="BTC", description="The symbol of the cryptocurrency to query, e.g., 'BTC'.")

class Variation(BaseModel):
    """
    Represents the variation information of a cryptocurrency.
    """
    string: str = Field(..., example="+1.80%", description="The variation percentage as a string.")
    number: float = Field(..., example=1.8, description="The variation percentage as a number.")
    status: str = Field(..., example="positive", description="The status of the variation (e.g., 'positive', 'negative').")

class CoinResponse(BaseModel):
    """
    Model to represent the response containing coin information.
    """
    total_items: int = Field(..., example=1, description="Total items in the response.")
    coin_name: str = Field(..., example="Bitcoin", description="The name of the cryptocurrency.")
    product_id: str = Field(..., example="BTC", description="The unique identifier for the cryptocurrency.")
    name: str = Field(..., example="Bitcoin", description="The name of the cryptocurrency.")
    icon_url: Dict[str, str] = Field(..., description="URLs for SVG and PNG icons.")
    type: str = Field(..., example="crypto", description="The type of asset.")
    market_price: str = Field(..., example="384186.00", description="The price of the cryptocurrency in BRL.")
    description: str = Field(..., example="A brief description of the cryptocurrency.", description="Description of the cryptocurrency.")
    symbol: str = Field(..., example="BTC", description="The symbol of the cryptocurrency.")
    variation: Variation = Field(..., description="Variation information of the cryptocurrency.")
    market_cap: str = Field(..., example="7596257266117", description="The market capitalization in BRL.")
    release_date: str = Field(..., example="2013-01-01", description="The release date of the cryptocurrency.")
    quote: str = Field(..., example="BRL", description="The currency of the market price.")
    coin_price: float = Field(..., example=384186.00, description="The price of the cryptocurrency in local currency (BRL).")
    coin_price_dolar: str = Field(..., example="75237.883138", description="The price of the cryptocurrency in USD.")
    date_consult: str = Field(..., example="2024-01-20 06:35:06", description="The date and time when the data was retrieved.")
