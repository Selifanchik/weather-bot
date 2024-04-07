import os

HOST = 'db:5432'
DIALECT = 'postgresql'

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

TOKEN = os.getenv('TOKEN')
TOKEN_WEATHER_API = os.getenv('TOKEN_WEATHER_API')