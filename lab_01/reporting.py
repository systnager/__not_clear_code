class Reporting:
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.invoices = []
        self.outvoices = []

    def register_incoming(self, product, delivery_date):
        self.warehouse.add_item(product, delivery_date)
        self.invoices.append({'product': product, 'delivery_date': delivery_date})

    def register_outgoing(self, product_name, quantity, delivery_date):
        self.warehouse.remove_item(product_name, quantity)
        self.outvoices.append({'product_name': product_name, 'quantity': quantity, 'delivery_date': delivery_date})

    def inventory_report(self):
        report = []
        for item in self.warehouse.items.values():
            product = item['product']
            report.append({
                'name': product.name,
                'unit': product.unit,
                'price': str(product.price),
                'quantity': item['quantity'],
                'delivery_date': item['delivery_date']
            })
        return report
    