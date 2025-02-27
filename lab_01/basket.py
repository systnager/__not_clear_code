from money import Money


class Basket:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_name, quantity):
        if product_name not in self.items or self.items[product_name]['quantity'] < quantity:
            raise ValueError("Not enough quantity in basket")
        self.items[product_name]['quantity'] -= quantity
        if self.items[product_name]['quantity'] == 0:
            del self.items[product_name]

    def total_cost(self):
        total = Money()
        for item in self.items.values():
            product = item['product']
            q = item['quantity']
            total.add_funds(product.price.get_whole_amount() * q, product.price.get_part_amount() * q)
        return total
