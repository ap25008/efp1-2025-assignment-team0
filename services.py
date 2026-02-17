from models import Product, InvoiceItem, Invoice

invoices = []


def register_invoice():
    print("\nΚαταχώρηση τιμολογίου")

    barcode = input("Barcode: ")
    name = input("Όνομα προϊόντος: ")
    category = input("Κατηγορία: ")
    price = float(input("Τιμή: "))
    quantity = int(input("Ποσότητα: "))
    package_type = input("Τύπος συσκευασίας: ")
    date = input("Ημερομηνία: ")

    product = Product(barcode, name, category, price)

    item = InvoiceItem(product, quantity, package_type)

    invoice = Invoice(len(invoices) + 1, date)
    invoice.items.append(item)

    invoices.append(invoice)

    print("Το τιμολόγιο καταχωρήθηκε.\n")