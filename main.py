from admin import Admin
from customer import Customer

def main():
    admin = Admin()
    customer_manager = Customer()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if admin.login():  
                while True:
                    print("\nAdmin Menu")
                    print("1. Show books")
                    print("2. Show customers")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        admin.show_books()
                    elif admin_choice == '2':
                        admin.show_customers()
                    elif admin_choice == '3':
                        print("Logging out as admin... Returning to main menu...")
                        break
                    else:
                        print("Invalid choice. Returning to admin menu...")

        elif choice == '2':
            print("\nCustomer Menu")
            print("1. Register")
            print("2. Login")
            print("3. Delete Account")
            print("4. Exit to Main Menu")
            customer_choice = input("Enter your choice: ")

            if customer_choice == '1':
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                confirm_password = input("Confirm password: ")
                customer_manager.register(username, email, password, confirm_password)

            elif customer_choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                account = customer_manager.login(username, password)
                if account and account.is_activated:
                    while True:  
                        print("\nCustomer Operations")
                        print("1. Buy Book")
                        print("2. Sell Book")
                        print("3. Search for Book")
                        print("4. Logout")
                        operation = input("Enter your choice: ")

                        if operation == '1':
                            book_name = input("Enter book name: ")
                            for book in admin.books:
                                if book['name'] == book_name:
                                    print(f"Original Price: {book['price']}")
                                    bargain_price = book['price'] * 0.75
                                    while True:
                                        customer_offer = float(input("Enter your bargain amount: "))
                                        if customer_offer >= bargain_price:
                                            print("Bargain accepted! Purchase successful.")
                                            admin.books.remove(book)
                                            break
                                        else:
                                            print("Bargain too low. Try again.")
                                    break
                            else:
                                print("Book not found.")

                        elif operation == '2':
                            book_name = input("Enter book name to sell: ")
                            price = float(input("Enter price: "))
                            admin.add_book(book_name, price)
                            print("Book added to library for sale.")

                        elif operation == '3':
                            book_name = input("Enter book name to search: ")
                            for book in admin.books:
                                if book['name'] == book_name:
                                    print(f"Book found: {book['name']} (Price: {book['price']})")
                                    break
                            else:
                                print("Book not found.")

                        elif operation == '4':
                            print("Logging out...")
                            break  

                        else:
                            print("Invalid choice. Please try again.")

            elif customer_choice == '3':
                username = input("Enter username: ")
                password = input("Enter password: ")
                customer_manager.delete_account(username, password)

            elif customer_choice == '4':
                print("Returning to main menu...")

            else:
                print("Invalid choice. Returning to main menu...")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()