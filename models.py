
# ΚΛΑΣΕΙΣ ΤΟΜΕΑ 
class Product:
    # Οντότητα προϊόντος του supermarket
    def __init__(self, barcode, name, category, price, min_limit, max_limit, units_per_pallet, units_per_box):
        self.barcode = barcode                     # Κωδικός barcode προϊόντος
        self.name = name                           # Όνομα προϊόντος
        self.category = category                   # Κατηγορία προϊόντος
        self.price = price                         # Τιμή προϊόντος
        self.min_limit = min_limit                 # Ελάχιστη ποσότητα
        self.max_limit = max_limit                 # Μέγιστη ποσότητα
        self.units_per_pallet = units_per_pallet   # Τεμάχια ανά παλλέτα
        self.units_per_box = units_per_box         # Τεμάχια ανά κιβώτιο


class InvoiceItem:
    # Οντότητα γραμμής τιμολογίου
    def __init__(self, product, quantity, package_type):
        self.product = product             # Προϊόν που παραλήφθηκε
        self.quantity = quantity           # Ποσότητα
        self.package_type = package_type   # Τύπος συσκευασίας


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


class OrderItem:
    # Οντότητα γραμμής παραγγελίας
    def __init__(self, product, quantity, package_text):
        self.product = product            # Το προϊόν που παραγγέλνουμε
        self.quantity = quantity          # Η τελική ποσότητα (σε τεμάχια)
        self.package_text = package_text  # Η περιγραφή της συσκευασίας (π.χ. "2 Παλ.")


class Order:
    # Οντότητα παραγγελίας προς προμηθευτή
    def __init__(self, order_id, date, status="Έχει υποβληθεί"):
        self.order_id = order_id  # Αριθμός παραγγελίας
        self.date = date          # Ημερομηνία καταχώρησης
        self.status = status      # Κατάσταση (default: "Έχει υποβληθεί")
        self.items = []           # Λίστα από OrderItem