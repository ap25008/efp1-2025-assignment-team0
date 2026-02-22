
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
    print("\nΚαταχώρηση Νέου Τιμολογίου Παραλαβής")
    date = input("Ημερομηνία Τιμολογίου (YYYY-MM-DD): ")
    invoice = Invoice(len(invoices) + 1, date)




    # Εισαγωγή δεδομένων από χρήστη


    
    while True:
        print("\nΣτοιχεία Προϊόντος")
        barcode = input("Barcode: ")
        name = input("Όνομα προϊόντος: ")
        category = input("Κατηγορία: ")
        price = float(input("Τιμή μονάδας: "))
        quantity_input = int(input("Συνολική ποσότητα παραλαβής (π.χ. 2 παλέτες, ή 5 κιβώτια): "))
        
        print("\nΕπιλέξτε τύπο συσκευασίας για αυτή την παραλαβή:")
        print("1. Παλέτα")
        print("2. Κιβώτιο")
        print("3. Τεμάχιο")
        pkg_choice = input("Επιλογή (1-3): ")
        pkg_map = {"1": "Παλέτα", "2": "Κιβώτιο", "3": "Τεμάχιο"}
        package_type = pkg_map.get(pkg_choice, "Τεμάχιο")

        u_pallet = 1
        u_box = 1
        total_pieces = quantity_input

        if pkg_choice == "1":
            u_pallet = int(input("Πόσα τεμάχια αντιστοιχούν σε 1 ΠΑΛΕΤΑ; "))
            total_pieces = quantity_input * u_pallet
        elif pkg_choice == "2":
            u_box = int(input("Πόσα τεμάχια αντιστοιχούν σε 1 ΚΙΒΩΤΙΟ; "))
            total_pieces = quantity_input * u_box

        min_l = int(input("Ελάχιστο όριο αποθέματος (Min): "))
        max_l = int(input("Μέγιστο όριο αποθέματος (Max): "))

    # Δημιουργία αντικειμένων
        product = Product(barcode, name, category, price, min_l, max_l, u_pallet, u_box)
        invoice.items.append(InvoiceItem(product, quantity_input, package_type))
        update_inventory(product, total_pieces)

        print(f"-> Ενσωματώθηκαν {quantity_input} {package_type} (Σύνολο: {total_pieces} τεμάχια) του προϊόντος {name}.")

        more = input("\nΥπάρχει άλλο προϊόν προς καταχώρηση σε αυτό το τιμολόγιο; (ναι/οχι): ").strip().lower()
        if more not in ['ν', 'ναι', 'y', 'yes', 'v']:
            break

    invoices.append(invoice)
    print(f" ΕΠΙΤΥΧΙΑ: Το Τιμολόγιο με ID '{invoice.invoice_id}' ολοκληρώθηκε και αποθηκεύτηκε!")

    print("Το τιμολόγιο καταχωρήθηκε.\n")

# Προβολή Τιμολογίων

def show_invoices():
    if not invoices:
        print("\nΔεν υπάρχουν καταχωρημένα τιμολόγια.")
        return
    print("\nΙΣΤΟΡΙΚΟ ΤΙΜΟΛΟΓΙΩΝ")
    for inv in invoices:
        print(f"\nID Τιμολογίου: {inv.invoice_id} | Ημερομηνία: {inv.date}")
        for it in inv.items:
            print(f"  -> {it.product.barcode} - {it.product.name}: {it.quantity} {it.package_type}")
# Προβολή Αποθέματος
def show_inventory():
    if not inventory:
        print("\nΤο απόθεμα είναι άδειο.")
        return
    print("\nΤΡΕΧΟΝ ΑΠΟΘΕΜΑ")
    print(f"{'BARCODE':<8} | {'ΠΡΟΪΟΝ':<12} | {'ΚΑΤΗΓΟΡΙΑ':<10} | {'ΤΙΜΗ':<6} | {'ΑΠΟΘΕΜΑ(ΤΕΜ)':<13} | {'MIN':<4} | {'MAX':<4}")
    for item in inventory:
        p = item.product
        print(f"{p.barcode:<8} | {p.name:<12} | {p.category:<10} | {p.price:<6.2f} | {item.quantity:<13} | {p.min_limit:<4} | {p.max_limit:<4}")

# Placeholder για Use Case Παραγγελίας

def create_order():
    print("\nΚαταχώρηση νέας παραγγελίας")
    print("Η λειτουργία δεν έχει υλοποιηθεί ακόμη.\n")