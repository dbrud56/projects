from pymongo import MongoClient


class MongoDBHandler:
    def __init__(self, db_name: str, uri: str = "mongodb://localhost:27017/"):
        self.client = MongoClient()
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]
