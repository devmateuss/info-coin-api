create_user_docs = {
    'tags': ['User'],
    'summary': 'Create a new user',
    'description': 'Creates a new user with a username and password.',
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
        '201': {
            'description': 'User created successfully.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'message': {
                                'type': 'string',
                                'example': 'User created successfully'
                            },
                            'username': {
                                'type': 'string',
                                'example': 'user@example.com'
                            }
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Validation error or user already exists.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'error': {
                                'type': 'string',
                                'example': 'Username and password are required'
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
