import os
from dotenv import load_dotenv

load_dotenv()


SPOT_CONFIG = {
    'apiKey': os.getenv('APIKEY'),
    'secret': os.getenv('SECRET'),
    'urls': {
        'api': {
            'api': 'https://api-demo.bybit.com',
        },
    },
    
    'options': {
        'defaultType': 'spot',
        'adjustForTimeDifference': True,
        'recvWindow': 15000, 
    },
    
    'enableRateLimit': True,
    # 'verbose': True,
}

LINEAR_CONFIG = {
    'apiKey': os.getenv('APIKEY'),
    'secret': os.getenv('SECRET'),
    'urls': {
        'api': {
            'api': 'https://api-demo.bybit.com',
        },
    },
    'options': {
        'defaultType': 'linear',
        'adjustForTimeDifference': True,
        'recvWindow': 15000, 
    },
    'enableRateLimit': True,
    # 'verbose': True,
}