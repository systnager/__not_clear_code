import unittest
from money import Money


money = Money()


class MoneyTestCase(unittest.TestCase):
    def test_add(self):
        money.add_funds(1, 105)
        self.assertEqual(money.get_whole_amount(), 2)
        self.assertEqual(money.get_part_amount(), 5)

    def test_minus(self):
        money.minus_funds(1, 105)
        self.assertEqual(money.get_whole_amount(), 0)
        self.assertEqual(money.get_part_amount(), 0)


if __name__ == "__main__":
    unittest.main()