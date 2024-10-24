from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.models.crypto_currency_model import ProductRequest, ProductResponse
from app.services.crypto_currency_bitcoin_market_service import CryptoCurrencyService

api_product = Blueprint('products', __name__)
service = CryptoCurrencyService()

@api_product.route('/', methods=['GET'])
def get_crypto_products():
    """
    Fetches cryptocurrency products from the external API.
    """
    try:
        # Parse query parameters using Pydantic's ProductRequest
        query = ProductRequest(**request.args)
        response = service.get_products(query)
        return jsonify(response.dict()), 200
    except ValidationError as e:
        # Return validation errors if parameters are incorrect
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        # Return a generic error message for other exceptions
        return jsonify({"error": str(e)}), 500
