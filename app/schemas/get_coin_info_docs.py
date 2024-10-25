get_coin_info_docs = {
    'tags': ['Crypto'],
    'summary': 'Get cryptocurrency information',
    'description': 'Fetches detailed information about a cryptocurrency based on the symbol provided and the specified provider.',
    'parameters': [
        {
            'name': 'provider',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The provider from which to fetch cryptocurrency information (e.g., mercadobitcoin, coingecko).',
            'example': 'mercadobitcoin'
        },
        {
            'name': 'symbol',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'The symbol of the cryptocurrency (e.g., BTC, ETH).',
            'example': 'BTC'
        }
    ],
    'responses': {
        '200': {
            'description': 'Cryptocurrency information retrieved successfully.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'total_items': {
                                'type': 'integer',
                                'example': 1,
                                'description': 'Total number of items in the response.'
                            },
                            'coin_name': {
                                'type': 'string',
                                'example': 'Bitcoin',
                                'description': 'The name of the cryptocurrency.'
                            },
                            'product_id': {
                                'type': 'string',
                                'example': 'BTC',
                                'description': 'The unique identifier for the cryptocurrency.'
                            },
                            'name': {
                                'type': 'string',
                                'example': 'Bitcoin',
                                'description': 'The name of the cryptocurrency.'
                            },
                            'icon_url': {
                                'type': 'object',
                                'properties': {
                                    'svg': {
                                        'type': 'string',
                                        'example': 'https://static.mercadobitcoin.com.br/web/img/icons/assets/ico-asset-btc-color.svg'
                                    },
                                    'png': {
                                        'type': 'string',
                                        'example': 'https://static.mercadobitcoin.com.br/app/general/assets/btc.png'
                                    }
                                }
                            },
                            'type': {
                                'type': 'string',
                                'example': 'crypto',
                                'description': 'Type of the asset.'
                            },
                            'market_price': {
                                'type': 'string',
                                'example': '380266.90',
                                'description': 'The current market price in BRL.'
                            },
                            'description': {
                                'type': 'string',
                                'example': 'Bitcoin is a digital currency...',
                                'description': 'Detailed description of the cryptocurrency.'
                            },
                            'symbol': {
                                'type': 'string',
                                'example': 'BTC',
                                'description': 'The symbol of the cryptocurrency.'
                            },
                            'variation': {
                                'type': 'object',
                                'properties': {
                                    'string': {
                                        'type': 'string',
                                        'example': '+1.80%',
                                        'description': 'The percentage change as a string.'
                                    },
                                    'number': {
                                        'type': 'number',
                                        'example': 1.8,
                                        'description': 'The percentage change as a number.'
                                    },
                                    'status': {
                                        'type': 'string',
                                        'example': 'positive',
                                        'description': 'The status of the variation (e.g., positive, negative).'
                                    }
                                }
                            },
                            'market_cap': {
                                'type': 'string',
                                'example': '7596257266117',
                                'description': 'Market capitalization in BRL.'
                            },
                            'release_date': {
                                'type': 'string',
                                'example': '2013-01-01',
                                'description': 'The release date of the cryptocurrency.'
                            },
                            'quote': {
                                'type': 'string',
                                'example': 'BRL',
                                'description': 'The currency of the market price.'
                            },
                            'coin_price': {
                                'type': 'number',
                                'example': 384186.00,
                                'description': 'The price of the cryptocurrency in local currency (BRL).'
                            },
                            'coin_price_dolar': {
                                'type': 'string',
                                'example': '75237.88',
                                'description': 'The price of the cryptocurrency in USD.'
                            },
                            'date_consult': {
                                'type': 'string',
                                'example': '2024-01-20 06:35:06',
                                'description': 'The date and time when the data was retrieved.'
                            }
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Validation error due to missing parameters.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'error': {
                                'type': 'string',
                                'example': 'Symbol query parameter is required.'
                            }
                        }
                    }
                }
            }
        },
        '500': {
            'description': 'Internal server error.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'error': {
                                'type': 'string',
                                'example': 'An unexpected error occurred.'
                            }
                        }
                    }
                }
            }
        }
    }
}
