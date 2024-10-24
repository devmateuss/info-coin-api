# src/models/crypto_currency_models.py

from pydantic import BaseModel, Field
from typing import List, Optional

class ProductRequest(BaseModel):
    symbol: str = Field(..., description="Cryptocurrency symbol", example="btc")

class IconUrl(BaseModel):
    svg: str
    png: str

class ProductData(BaseModel):
    symbol: str
    type: str
    sub_type: dict
    variation: dict
    market_cap: str
    created_at: str
    release_date: str
    asset_decimals: int
    fiat_decimals: int
    visible_when_unlogged: bool
    visible_when_logged: bool
    prelisted: bool
    quote: str
    cover_letter_data: dict

class Balances(BaseModel):
    available_quantity: str
    available_fiat_value: str
    on_hold_quantity: str
    on_hold_fiat_value: str

class ProductItem(BaseModel):
    product_id: str
    name: str
    icon_url: IconUrl
    type: str
    market_price: str
    tags: List[str]
    description: str
    product_data: ProductData
    favorite: bool
    balances: Balances
    visible_when_logged: bool
    visible_when_unlogged: bool

class ProductResponse(BaseModel):
    total_items: int
    response_data: dict
