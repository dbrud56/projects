import unittest
from unittest.mock import patch, MagicMock
from mongodb.producthandler import ProductDatabaseHandler, Product


class TestProductDatabaseHandler(unittest.TestCase):
    @patch("mongodb.dbhandler.MongoDBHandler.get_collection")
    def setUp(self, mock_get_collection):
        self.mock_collection = MagicMock()
        mock_get_collection.return_value = self.mock_collection
        self.handler = ProductDatabaseHandler()

    def test_insert(self):
        product = Product(product_id=1, name="Test Product", price=100, stock=10)
        self.mock_collection.insert_one.return_value.inserted_id = "mock_id"
        result = self.handler.insert(product)

        self.mock_collection.insert_one.assert_called_once_with(product.__dict__)
        self.assertEqual(result, "mock_id")

    def test_find(self):
        product = Product(product_id=1, name="Test Product", price=100, stock=10)
        self.mock_collection.find_one.return_value = product
        result = self.handler.find(1)

        self.mock_collection.find_one.assert_called_once_with({"product_id": 1})
        self.assertEqual(result, product)

    def test_update(self):
        self.mock_collection.update_one.return_value.modified_count = 1
        result = self.handler.update(1, {"price": 150})

        self.mock_collection.update_one.assert_called_once_with(
            {"product_id": 1}, {"$set": {"price": 150}}
        )

        self.assertEqual(result, 1)

    def test_delete(self):
        self.mock_collection.delete_many.return_value.deleted_count = 1
        result = self.handler.delete(1)

        self.mock_collection.delete_many.assert_called_once_with({"product_id": 1})
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
