class Product:
    def __init__(self, name, unit, price, quantity, category=None):
        self.name = name
        self.unit = unit
        self.price = price
        self.quantity = quantity
        self.category = category
    def reduce_price(self, reduction):
        new_total = self.price.total_cents() - reduction.total_cents()
        if new_total < 0:
            raise ValueError("Price cannot be negative")
        self.price.set_funds(new_total // 100, new_total % 100)
