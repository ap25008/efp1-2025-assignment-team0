
# ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ 

from services import register_invoice, show_invoices, update_inventory, show_inventory, create_order, get_packaging_info


def main():
    while True:
        print("\nΣύστημα Supermarket")
        print("1. Καταχώρηση τιμολογίου")
        print("2. Προβολή τιμολογίων")
        print("3. Προβολή αποθέματος")
        print("4. Καταχώρηση νέας παραγγελίας")
        print("5. Προβολή παραγγελιών")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            register_invoice()
        elif choice == "2":
            show_invoices()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            create_order()
        elif choice == "5":
            show_orders()
        elif choice == "0":
            print("Έξοδος...")
            break
        else:
            print("Μη έγκυρη επιλογή\n")


# Εκτελείται μόνο όταν τρέχουμε το αρχείο άμεσα
if __name__ == "__main__":
    main()