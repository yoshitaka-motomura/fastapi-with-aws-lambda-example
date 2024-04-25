from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

"""Database Access Credentials"""

MONGO_USER = os.getenv('MONGO_USER')
MONGO_USER_PASSWORD = os.getenv('MONGO_USER_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_APP_NAME = os.getenv('MONGO_APP_NAME')

"""MongoDB URI"""
MONGO_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_USER_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority&appName={MONGO_APP_NAME}'


def get_db():
    client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
    db = client['app']
    return db
