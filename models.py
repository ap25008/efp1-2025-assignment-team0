
# ΚΛΑΣΕΙΣ ΤΟΜΕΑ 
class Product:
    # Οντότητα προϊόντος του supermarket
    def __init__(self, barcode, name, category, price):
        self.barcode = barcode      # Κωδικός barcode προϊόντος
        self.name = name            # Όνομα προϊόντος
        self.category = category    # Κατηγορία προϊόντος
        self.price = price          # Τιμή προϊόντος


class InvoiceItem:
    # Οντότητα γραμμής τιμολογίου
    def __init__(self, product, quantity, package_type):
        self.product = product          # Προϊόν που παραλήφθηκε
        self.quantity = quantity        # Ποσότητα
        self.package_type = package_type  # Τύπος συσκευασίας


class Invoice:
    # Οντότητα τιμολογίου παραλαβής
    def __init__(self, invoice_id, date):
        self.invoice_id = invoice_id  # Κωδικός τιμολογίου
        self.date = date              # Ημερομηνία παραλαβής
        self.items = []               # Λίστα από InvoiceItem


class InventoryItem:
    # Οντότητα αποθέματος ενός προϊόντος
    def __init__(self, product, quantity):
        self.product = product      # Προϊόν
        self.quantity = quantity    # Διαθέσιμη ποσότητα