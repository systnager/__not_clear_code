import unittest
from money import Money
from product import Product
from warehouse import Warehouse
from reporting import Reporting
from basket import Basket

class MoneyTestCase(unittest.TestCase):
    def setUp(self):
        self.money = Money()
    def test_add(self):
        self.money.add_funds(1, 105)
        self.assertEqual(self.money.get_whole_amount(), 2)
        self.assertEqual(self.money.get_part_amount(), 5)
    def test_minus(self):
        self.money.add_funds(1, 105)
        self.money.minus_funds(1, 105)
        self.assertEqual(self.money.get_whole_amount(), 0)
        self.assertEqual(self.money.get_part_amount(), 0)
    def test_set_funds(self):
        self.money.set_funds(3, 250)
        self.assertEqual(self.money.get_whole_amount(), 5)
        self.assertEqual(self.money.get_part_amount(), 50)
    def test_total_cents(self):
        self.money.set_funds(2, 50)
        self.assertEqual(self.money.total_cents(), 250)

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.price = Money()
        self.price.set_funds(10, 0)
        self.product = Product("Apple", "kg", self.price, 100, "Fruit")
    def test_reduce_price(self):
        reduction = Money()
        reduction.set_funds(2, 0)
        self.product.reduce_price(reduction)
        self.assertEqual(self.product.price.get_whole_amount(), 8)
        self.assertEqual(self.product.price.get_part_amount(), 0)
    def test_reduce_price_exception(self):
        reduction = Money()
        reduction.set_funds(20, 0)
        with self.assertRaises(ValueError):
            self.product.reduce_price(reduction)

class WarehouseTestCase(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse()
        self.price = Money()
        self.price.set_funds(5, 50)
        self.product = Product("Milk", "liter", self.price, 50, "Dairy")
    def test_add_item(self):
        self.warehouse.add_item(self.product, "2025-02-27")
        self.assertIn("Milk", self.warehouse.items)
        self.assertEqual(self.warehouse.items["Milk"]['quantity'], 50)
    def test_remove_item(self):
        self.warehouse.add_item(self.product, "2025-02-27")
        self.warehouse.remove_item("Milk", 20)
        self.assertEqual(self.warehouse.items["Milk"]['quantity'], 30)
        with self.assertRaises(ValueError):
            self.warehouse.remove_item("Milk", 40)
    def test_remove_item_complete(self):
        self.warehouse.add_item(self.product, "2025-02-27")
        self.warehouse.remove_item("Milk", 50)
        self.assertNotIn("Milk", self.warehouse.items)

class ReportingTestCase(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse()
        self.reporting = Reporting(self.warehouse)
        self.price = Money()
        self.price.set_funds(3, 75)
        self.product = Product("Bread", "pc", self.price, 30, "Bakery")
    def test_register_incoming(self):
        self.reporting.register_incoming(self.product, "2025-02-27")
        self.assertIn("Bread", self.warehouse.items)
        self.assertEqual(len(self.reporting.invoices), 1)
    def test_register_outgoing(self):
        self.reporting.register_incoming(self.product, "2025-02-27")
        self.reporting.register_outgoing("Bread", 10, "2025-02-28")
        self.assertEqual(self.warehouse.items["Bread"]['quantity'], 20)
        self.assertEqual(len(self.reporting.outvoices), 1)
    def test_inventory_report(self):
        self.reporting.register_incoming(self.product, "2025-02-27")
        report = self.reporting.inventory_report()
        self.assertEqual(report[0]['name'], "Bread")
        self.assertEqual(report[0]['unit'], "pc")

class BasketTestCase(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()
        self.price = Money()
        self.price.set_funds(2, 30)
        self.product = Product("Eggs", "dozen", self.price, 10, "Poultry")
    def test_add_remove_product(self):
        self.basket.add_product(self.product, 2)
        self.assertIn("Eggs", self.basket.items)
        self.basket.remove_product("Eggs", 1)
        self.assertEqual(self.basket.items["Eggs"]['quantity'], 1)
        self.basket.remove_product("Eggs", 1)
        self.assertNotIn("Eggs", self.basket.items)
    def test_total_cost(self):
        self.basket.add_product(self.product, 3)
        total = self.basket.total_cost()
        self.assertEqual(total.get_whole_amount(), 6)
        self.assertEqual(total.get_part_amount(), 90)

if __name__ == "__main__":
    unittest.main()
