
import math
import datetime  #Εισαγωγή βιβλιοθήκης για ημερομηνία και ώρα

# (Use Cases)


from models import Product, InvoiceItem, Invoice, InventoryItem

# Λίστα αποθηκευμένων τιμολογίων
invoices = []

# Λίστα αποθέματος
inventory = []

# Λίστα αποθηκευμένων παραγγελιών
orders = []

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
        print(f"{item.product.name} - {item.quantity} τεμάχια")

# Προβολή Παραγγελιών
def show_orders():
    if not orders:
        print("\nΔεν υπάρχουν καταχωρημένες παραγγελίες.\n")
        return

    print("\nΛίστα Παραγγελιών:")
    for order in orders:
        print(f"\nΠαραγγελία #{order.order_id} - Ημερομηνία: {order.date} - Κατάσταση: {order.status}")
        print(f"{'ΠΡΟΪΟΝ':<15} | {'ΠΟΣΟΤΗΤΑ':<10} | {'ΣΥΣΚΕΥΑΣΙΑ'}")
        print("-" * 45)
        for item in order.items:
            print(f"{item.product.name:<15} | {item.quantity:<10} | {item.package_text}")


    #Στρογγυλοποίηση προς τα πάνω στο είδος που παραγγέλνεται
def get_packaging_info(pieces, prod):
    if pieces == 0: return "Ακυρώθηκε", 0
        
    if prod.units_per_pallet != 1:
            pallets = math.ceil(pieces / prod.units_per_pallet)
            return f"{pallets} Παλ.", pallets * prod.units_per_pallet
    elif prod.units_per_box != 1:
            boxes = math.ceil(pieces / prod.units_per_box)
            return f"{boxes} Κιβ.", boxes * prod.units_per_box
    else:
            return f"{pieces} Τεμ.", pieces



# Use Case: Δημιουργία Παραγγελίας

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

    # 2. Αρχική Εισαγωγή Ποσοτήτων από τον Διευθυντή
    print("\n ΑΡΧΙΚΗ ΕΠΕΞΕΡΓΑΣΙΑ ΔΙΕΥΘΥΝΤΗ")
    for barcode, entry in draft_orders.items():
        p = entry['product']
        print(f"\nΠροϊόν: {p.barcode} | {p.name} (Τρέχον Απόθεμα: {entry['current_qty']})")
        print(f"Πρόταση Συστήματος: {entry['sys_text']} (Η οποία καλύπτει {entry['sys_pieces']} τεμάχια)")
        
        choice = input(f"Πόσα συνολικά ΤΕΜΑΧΙΑ θέλετε να παραγγείλετε; (Enter για αποδοχή των {entry['sys_pieces']}): ")
        
        if choice.strip():
            input_pieces = int(choice)
            new_text, new_total = get_packaging_info(input_pieces, p)
            entry['final_pieces'] = new_total
            entry['final_text'] = new_text
            print(f"-> Το σύστημα στρογγυλοποίησε την επιλογή σας σε: {new_text} (Σύνολο: {new_total} τεμ.)")


    # 3. Βρόχος (Loop) Προεπισκόπησης και Υποβολής/Τροποποίησης
    while True:
        print("ΠΡΟΕΠΙΣΚΟΠΗΣΗ ΠΑΡΑΓΓΕΛΙΑΣ")
        print(f"{'BARCODE':<10} | {'ΠΡΟΪΟΝ':<15} | {'ΠΟΣΟΤΗΤΑ (ΤΕΜ)':<15} | {'ΤΕΛΙΚΕΣ ΣΥΣΚΕΥΑΣΙΕΣ'}")
        
        for barcode, entry in draft_orders.items():
            if entry['final_pieces'] > 0:
                print(f"{barcode:<10} | {entry['product'].name:<15} | {entry['final_pieces']:<15} | {entry['final_text']}")
        
        print("\nΕπιλογές:")
        print("1. Υποβολή (Οριστικοποίηση της παραγγελίας)")
        print("2. Τροποποίηση (Αλλαγή ποσότητας σε συγκεκριμένο προϊόν)")
        
        action = input("Επιλέξτε ενέργεια (1 ή 2): ")
        
        if action == "1":
            # Χρήση των κλάσεων Order και OrderItem 
            today_date = datetime.date.today().strftime("%Y-%m-%d")
            order_number = len(orders) + 1
            
            # Δημιουργία του αντικειμένου Order
            new_order = Order(order_number, today_date)

            # Προσθήκη των προϊόντων (OrderItems) μέσα στην παραγγελία
            for barcode, entry in draft_orders.items():
                if entry['final_pieces'] > 0:
                    order_item = OrderItem(entry['product'], entry['final_pieces'], entry['final_text'])
                    new_order.items.append(order_item)
            
            # Αποθήκευση της νέας παραγγελίας στη λίστα
            orders.append(new_order)

            # Εμφάνιση των στοιχείων της παραγγελίας
            print(" ΕΠΙΤΥΧΙΑ: Η παραγγελία υποβλήθηκε επιτυχώς!")
            print(f" Αριθμός Παραγγελίας : {new_order.order_id}")
            print(f" Ημερομηνία          : {new_order.date}")
            print(f" Κατάσταση           : {new_order.status}")
            break

        elif action == "2":
            target_barcode = input("\nΕισάγετε το Barcode του προϊόντος προς τροποποίηση: ")
            
            if target_barcode in draft_orders:
                entry = draft_orders[target_barcode]
                p = entry['product']
                print(f"\nΕπιλεγμένο προϊόν: {p.name} | Τρέχουσα επιλογή: {entry['final_text']} ({entry['final_pieces']} τεμ.)")
                
                new_choice = input("Εισάγετε τη νέα επιθυμητή ποσότητα σε τεμάχια: ")
                if new_choice.strip():
                    input_pieces = int(new_choice)
                    new_text, new_total = get_packaging_info(input_pieces, p)
                    entry['final_pieces'] = new_total
                    entry['final_text'] = new_text
                    print(f"-> Η ποσότητα ενημερώθηκε και στρογγυλοποιήθηκε σε {new_text} ({new_total} τεμ.)!")
            else:
                print("-> Σφάλμα: Το Barcode δεν βρέθηκε στη λίστα της τρέχουσας παραγγελίας.")
        else:
            print("-> Λάθος επιλογή. Παρακαλώ πληκτρολογήστε 1 ή 2.")