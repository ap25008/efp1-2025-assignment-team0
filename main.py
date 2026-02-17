from services import register_invoice

def main():
    while True:
        print("1. Καταχώρηση τιμολογίου")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            register_invoice()
        elif choice == "0":
            break
        else:
            print("Μη έγκυρη επιλογή\n")


if __name__ == "__main__":
    main()


