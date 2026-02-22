
# (Use Cases)


from models import Product, InvoiceItem, Invoice, InventoryItem

# Λίστα αποθηκευμένων τιμολογίων
invoices = []

# Λίστα αποθέματος
inventory = []

# INCLUDE USE CASE: Ενημέρωση Αποθέματος

def update_inventory(product, quantity):
    # Ελέγχει αν το προϊόν υπάρχει ήδη στο απόθεμα
    for item in inventory:
        if item.product.barcode == product.barcode:
            # Αν υπάρχει, αυξάνει την ποσότητα
            item.quantity += quantity
            return

    # Αν δεν υπάρχει, δημιουργεί νέο InventoryItem
    inventory.append(InventoryItem(product, quantity))

# ΒΑΣΙΚΟ USE CASE: Καταχώρηση Τιμολογίου
def register_invoice():
    print("\nKαταχώρηση τιμολογίου")

    # Εισαγωγή δεδομένων από χρήστη
    barcode = input("Barcode: ")
    name = input("Όνομα προϊόντος: ")
    category = input("Κατηγορία: ")
    price = float(input("Τιμή (π.χ. 2.5): "))
    quantity = int(input("Ποσότητα: "))
    package_type = input("Τύπος συσκευασίας: ")
    date = input("Ημερομηνία (YYYY-MM-DD): ")

    # Δημιουργία αντικειμένων
    product = Product(barcode, name, category, price)
    item = InvoiceItem(product, quantity, package_type)

    # Δημιουργία τιμολογίου με αυτόματο ID
    invoice = Invoice(len(invoices) + 1, date)
    invoice.items.append(item)

    # INCLUDE: Ενημέρωση αποθέματος
    update_inventory(product, quantity)

    # Αποθήκευση τιμολογίου
    invoices.append(invoice)

    print("Το τιμολόγιο καταχωρήθηκε.\n")

# Προβολή Τιμολογίων

def show_invoices():
    if not invoices:
        print("Δεν υπάρχουν τιμολόγια.\n")
        return

    for invoice in invoices:
        print(f"\nΤιμολόγιο {invoice.invoice_id} - Ημερομηνία: {invoice.date}")
        for item in invoice.items:
            print(f"  Προϊόν: {item.product.name}")
            print(f"  Ποσότητα: {item.quantity}")
            print(f"  Συσκευασία: {item.package_type}")

# Προβολή Αποθέματος
def show_inventory():
    if not inventory:
        print("Το απόθεμα είναι κενό.\n")
        return

    print("\nΑπόθεμα:")
    for item in inventory:
        print(f"{item.product.name} - {item.quantity} τεμάχια")



# Placeholder για Use Case Παραγγελίας

def create_order():
    print(f"{'BARCODE':<8} | {'ΠΡΟΪΟΝ':<12} | {'ΚΑΤΗΓΟΡΙΑ':<10} | {'ΑΠΟΘΕΜΑ':<7} | {'ΕΛΛΕΙΜΜΑ':<8} | {'ΠΡΟΤΑΣΗ ΑΝΑΠΛΗΡΩΣΗΣ'}")

    draft_orders = {}

    
 # 1. Παραγωγή αρχικής πρότασης από το σύστημα
    for item in inventory:
        p = item.product
        if item.quantity <= p.min_limit:
            needed = p.max_limit - item.quantity
            
            # Υπολογισμός νέας καθαρής πρότασης
            proposal_text, total_prop_pieces = get_packaging_info(needed, p)
            
            draft_orders[p.barcode] = {
                'product': p,
                'current_qty': item.quantity,
                'sys_needed': needed,
                'sys_text': proposal_text,
                'sys_pieces': total_prop_pieces,
                'final_pieces': total_prop_pieces,
                'final_text': proposal_text
            }
            
            print(f"{p.barcode:<8} | {p.name:<12} | {p.category:<10} | {item.quantity:<7} | {needed:<8} | {proposal_text}")

    if not draft_orders:
        print("Το απόθεμα είναι επαρκές. Δεν απαιτείται παραγγελία.")
        return

