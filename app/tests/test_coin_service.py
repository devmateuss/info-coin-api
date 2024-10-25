import pytest
from unittest.mock import MagicMock
from pydantic import ValidationError
from app.models.coin_models import CoinRequest, CoinResponse, Variation


@pytest.fixture
def expected_response():
    return CoinResponse(
        total_items=1,
        coin_name="Bitcoin",
        product_id="BTC",
        name="Bitcoin",
        icon_url={"svg": "https://example.com/bitcoin.svg", "png": "https://example.com/bitcoin.png"},
        type="crypto",
        market_price="384186.00",
        description="A brief description of Bitcoin.",
        symbol="BTC",
        variation=Variation(string="+1.80%", number=1.8, status="positive"),
        market_cap="7596257266117",
        release_date="2013-01-01",
        quote="BRL",
        coin_price=384186.00,
        coin_price_dolar="75237.88",
        date_consult="2024-10-24T00:00:00Z"
    )

def test_get_coin_info_with_coingecko_success(coin_service, mocker, expected_response):
    request = CoinRequest(symbol="BTC")

    mock_repository = MagicMock()
    mock_repository.get_coin_info.return_value = expected_response

    mocker.patch('app.factories.crypto_factory.CryptoFactory.create', return_value=mock_repository)

    response = coin_service.get_coin_info(request, provider="coingecko")
    
    assert response == expected_response
    mock_repository.get_coin_info.assert_called_once_with(request)

def test_get_coin_info_with_mercadobitcoin_success(coin_service, mocker, expected_response):
    request = CoinRequest(symbol="BTC")

    mock_repository = MagicMock()
    mock_repository.get_coin_info.return_value = expected_response

    mocker.patch('app.factories.crypto_factory.CryptoFactory.create', return_value=mock_repository)

    response = coin_service.get_coin_info(request, provider="mercadobitcoin")
    
    assert response == expected_response
    mock_repository.get_coin_info.assert_called_once_with(request)

def test_get_coin_info_invalid_provider(coin_service, mocker):
    request = CoinRequest(symbol="BTC")

    mocker.patch('app.factories.crypto_factory.CryptoFactory.create', side_effect=ValueError("Invalid provider"))

    with pytest.raises(ValueError, match="Invalid provider"):
        coin_service.get_coin_info(request, provider="unknownprovider")

def test_get_coin_info_repository_error(coin_service, mocker):
    request = CoinRequest(symbol="BTC")

    mock_repository = MagicMock()
    mock_repository.get_coin_info.side_effect = Exception("API communication error")

    mocker.patch('app.factories.crypto_factory.CryptoFactory.create', return_value=mock_repository)

    with pytest.raises(Exception, match="API communication error"):
        coin_service.get_coin_info(request, provider="coingecko")


def test_get_coin_info_success_with_different_provider(coin_service, mocker):
    request = CoinRequest(symbol="ETH")
    expected_response = CoinResponse(
        total_items=1,
        coin_name="Ethereum",
        product_id="ETH",
        name="Ethereum",
        icon_url={"svg": "https://example.com/ethereum.svg", "png": "https://example.com/ethereum.png"},
        type="crypto",
        market_price="12000.00",
        description="A brief description of Ethereum.",
        symbol="ETH",
        variation=Variation(string="-0.50%", number=-0.5, status="negative"),
        market_cap="300000000000",
        release_date="2015-07-30",
        quote="BRL",
        coin_price=12000.00,
        coin_price_dolar="2500.00",
        date_consult="2024-10-24T00:00:00Z"
    )

    mock_repository = MagicMock()
    mock_repository.get_coin_info.return_value = expected_response

    mocker.patch('app.factories.crypto_factory.CryptoFactory.create', return_value=mock_repository)

    response = coin_service.get_coin_info(request, provider="another_provider")
    
    assert response == expected_response
    mock_repository.get_coin_info.assert_called_once_with(request)
