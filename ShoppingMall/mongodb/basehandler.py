from pymongo import MongoClient


class BaseDatabaseHandler:
    def __init__(self, db_name: str, collection_name: str, uri: str = "mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.collection = self.client[db_name][collection_name]

    def insert(self, product: dict):
        result = self.collection.insert_one(product)
        return result.inserted_id

    def find(self, product_id: int):
        product = self.collection.find_one({"product_id": product_id})
        return product

    def update(self, product_id: int, updated_data: dict):
        result = self.collection.update_one({"product_id": product_id}, {"$set": updated_data})
        return result.modified_count

    def delete(self, product_id: int):
        result = self.collection.delete_many({"product_id": product_id})
        return result.deleted_count
