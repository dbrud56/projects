from dataclasses import dataclass

from .dbhandler import MongoDBHandler


@dataclass
class Product:
    product_id: int
    name: str
    price: int
    stock: int


class ProductDatabaseHandler(MongoDBHandler):
    def __init__(self):
        self.collection = self.get_collection("Products")

    def insert(self, product: Product):
        product_dict = product.__dict__
        result = self.collection.insert_one(product_dict)
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
