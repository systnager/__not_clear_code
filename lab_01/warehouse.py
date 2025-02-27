class Warehouse:
    def __init__(self):
        self.items = {}

    def add_item(self, product, delivery_date):
        if not product.name in self.items:
            self.items[product.name] = {
                'product': product,
                'quantity': product.quantity,
                'price': product.price,
                'delivery_date': delivery_date
            }
            return

        existing = self.items[product.name]
        existing['quantity'] += product.quantity
        existing['price'] = product.price
        existing['delivery_date'] = delivery_date

    def remove_item(self, product_name, quantity):
        if product_name not in self.items or self.items[product_name]['quantity'] < quantity:
            raise ValueError("Not enough quantity")
        self.items[product_name]['quantity'] -= quantity
        if self.items[product_name]['quantity'] == 0:
            del self.items[product_name]