class Product:
    def __init__(self, barcode, name, category, price):
        self.barcode = barcode
        self.name = name
        self.category = category
        self.price = price


class InvoiceItem:
    def __init__(self, product, quantity, package_type):
        self.product = product
        self.quantity = quantity
        self.package_type = package_type


class Invoice:
    def __init__(self, invoice_id, date):
        self.invoice_id = invoice_id
        self.date = date
        self.items = []
