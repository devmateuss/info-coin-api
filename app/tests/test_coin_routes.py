from unittest.mock import patch

import jwt
import pytest


@pytest.fixture
def coin_data():
    return {
        "coin_name": "Bitcoin",
        "coin_price": 50000,
        "coin_price_dolar": 50000,
        "date_consult": "2024-10-24",
        "symbol": "BTC"
    }

def test_get_coin_info_success(client, coin_data, auth_token, mock_jwt_decode, app):
    mock_response = {
        "coin_name": "Bitcoin",
        "symbol": "BTC",
        "coin_price": 30000,
        "coin_price_dolar": 30000,
        "date_consult": "2024-10-24T00:00:00Z"
    }
    
    with patch('app.routes.coin_routes.service.get_coin_info', return_value=mock_response):
        response = client.get('/api/infocoin/coingecko?symbol=BTC', headers={"Authorization": auth_token})

        assert response.status_code == 200
        data = response.get_json()
        assert data["coin_name"] == "Bitcoin"
        assert data["symbol"] == "BTC"
        assert data["coin_price"] == 30000

def test_get_coin_info_missing_symbol(client, auth_token, mock_jwt_decode):
    response = client.get('/api/infocoin/coingecko', headers={"Authorization": auth_token})

    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Symbol query parameter is required"


def test_get_coin_info_service_error(client, auth_token, mock_jwt_decode):
    with patch('app.routes.coin_routes.service.get_coin_info', side_effect=Exception("Unexpected error")):
        response = client.get('/api/infocoin/coingecko?symbol=BTC', headers={"Authorization": auth_token})

        assert response.status_code == 500
        data = response.get_json()
        assert data["error"] == "Unexpected error"

def test_get_coin_info_symbol_not_found(client, auth_token, mock_jwt_decode):
    with patch('app.routes.coin_routes.service.get_coin_info', side_effect=ValueError("Symbol not found")):
        response = client.get('/api/infocoin/coingecko?symbol=UNKNOWN', headers={"Authorization": auth_token})

        assert response.status_code == 400
        data = response.get_json()
        assert data["error"] == "Symbol not found"


def test_get_coin_info_success_with_different_provider(client, coin_data, auth_token, mock_jwt_decode):
    mock_response = {
        "coin_name": "Ethereum",
        "symbol": "ETH",
        "coin_price": 2000,
        "coin_price_dolar": 2000,
        "date_consult": "2024-10-24T00:00:00Z"
    }
    
    with patch('app.routes.coin_routes.service.get_coin_info', return_value=mock_response):
        response = client.get('/api/infocoin/another_provider?symbol=ETH', headers={"Authorization": auth_token})

        assert response.status_code == 200
        data = response.get_json()
        assert data["coin_name"] == "Ethereum"
        assert data["symbol"] == "ETH"
        assert data["coin_price"] == 2000


def test_get_coin_info_invalid_token(client):
    invalid_token = 'Bearer invalid.jwt.token'
    response = client.get('/api/infocoin/coingecko?symbol=BTC', headers={"Authorization": invalid_token})

    assert response.status_code == 401
    data = response.get_json()
    assert data["error"] == "Invalid token"


def test_get_coin_info_expired_token(client, mock_jwt_decode):
    with patch('app.common.auth_decorator.jwt.decode', side_effect=jwt.ExpiredSignatureError):
        response = client.get('/api/infocoin/coingecko?symbol=BTC', headers={"Authorization": "Bearer expired.jwt.token"})

        assert response.status_code == 401
        data = response.get_json()
        assert data["error"] == "Token has expired"
