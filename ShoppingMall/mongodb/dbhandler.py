from dataclasses import dataclass

from .basehandler import BaseDatabaseHandler


@dataclass
class Product:
    product_id: int
    name: str
    price: int
    stock: int


@dataclass
class Order:
    order_id: int
    user_id: int
    products: dict
    total_price: int
    status: str


class ProductDatabaseHandler(BaseDatabaseHandler):
    def __init__(self):
        super().__init__("ShoppingMall", "Products")


class OrderDatabaseHandler(BaseDatabaseHandler):
    def __init__(self):
        super().__init__("ShoppingMall", "Orders")
