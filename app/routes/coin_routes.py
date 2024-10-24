from flask import Blueprint, request, jsonify
from app.models.coin_models import CoinRequest
from app.services.coin_service import CoinService

api_coin = Blueprint('coin', __name__)
service = CoinService()

@api_coin.route('/<provider>', methods=['GET'])
def get_coin_info(provider):
    """
    Fetches cryptocurrency info using the specified provider in the URL.
    """
    try:
        symbol = request.args.get('symbol')
        if not symbol:
            return jsonify({"error": "Symbol query parameter is required"}), 400

        coin_request = CoinRequest(symbol=symbol)
        
        response = service.get_coin_info(coin_request, provider)
        return jsonify(response.dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
