

class Admin:
    def __init__(self):
        self.books = []
        self.customers = []
        self.username = "teju"
        self.password = "123"  

    def login(self):
        print("\nAdmin Login")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == self.username and password == self.password:
            print("Admin login successful!")
            return True
        else:
            print("Invalid credentials. Returning to main menu...")
            return False

    def add_book(self, book_name, price):
        self.books.append({'name': book_name, 'price': price})
        print(f"Book '{book_name}' added successfully with price {price}.")

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(f"- {book['name']} (Price: {book['price']})")

    def show_customers(self):
        if not self.customers:
            print("No registered customers.")
        else:
            print("\nRegistered Customers:")
            for customer in self.customers:
                print(f"- Username: {customer.username}, Email: {customer.email}, Activated: {customer.is_activated}")

