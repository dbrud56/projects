import unittest
from unittest.mock import patch, MagicMock
from mongodb import BaseHandler, ProductDatabaseHandler, OrderDatabaseHandler


class TestBaseHandler(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.mock_collection = MagicMock()
        self.mock_client.__getitem__.return_value = self.mock_collection
        self.handler = BaseHandler("ShoppingMall", "Products")
        self.handler.client = self.mock_client
        self.handler.collection = self.mock_collection

    def tearDown(self):
        self.mock_client.close()
        self.handler.client.close()

    def test_insert(self):
        product = {"product_id": 1, "name": "Test Product", "price": 100, "stock": 10}
        self.mock_collection.insert_one.return_value.inserted_id = 1
        result = self.handler.insert(product)

        self.mock_collection.insert_one.assert_called_once_with(product)
        self.assertEqual(result, 1)

    def test_find(self):
        product = {"product_id": 1, "name": "Test Product", "price": 100, "stock": 10}
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


class TestProductDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ProductDatabaseHandler()

    def test_inheritance(self):
        self.assertTrue(issubclass(ProductDatabaseHandler, BaseHandler))


class TestOrderDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.handler = OrderDatabaseHandler()

    def test_inheritance(self):
        self.assertTrue(issubclass(OrderDatabaseHandler, BaseHandler))


if __name__ == "__main__":
    unittest.main()
