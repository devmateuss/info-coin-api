auth_scheme = {
    'tags': ['Authentication'],
    'summary': 'User login',
    'description': 'Generates a JWT token for authentication.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {
                        'type': 'string',
                        'example': 'mercadobitcoin@gmail.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'mercadobitcoin2024'
                    }
                },
                'required': ['username', 'password']
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Successful login.',
            'schema': {
                'type': 'object',
                'properties': {
                    'access_token': {
                        'type': 'string',
                        'description': 'JWT token for authentication'
                    }
                }
            }
        },
        '400': {
            'description': 'Field validation error.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string'
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid credentials.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}
