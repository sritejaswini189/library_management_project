
from customeracc import CustomerAccount

class Customer:
    def __init__(self):
        self.accounts = []

    def register(self, username, email, password, confirm_password):
        if password != confirm_password:
            print("Passwords do not match. Please re-enter your details.")
            return
        new_account = CustomerAccount(username, email, password)
        self.accounts.append(new_account)
        print("Registration successful! Returning to main menu...")

    def login(self, username, password):
        for account in self.accounts:
            if account.username == username and account.password == password:
                print("Login successful!")
                if not account.is_activated:
                    print("Your account is not activated. Please deposit an amount of at least 1000 for activation.")
                    amount = float(input("Enter amount: "))
                    if amount >= 1000:
                        account.is_activated = True
                        account.balance += amount
                        print("Account activation successful! Returning to main menu...")
                    else:
                        print("Activation failed. Amount must be at least 1000. Returning to main menu...")
                return account
        print("Invalid username or password. Returning to main menu...")
        return None

    def delete_account(self, username, password):
        for account in self.accounts:
            if account.username == username and account.password == password:
                confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()
                if confirmation == 'yes':
                    refund_amount = account.balance
                    self.accounts.remove(account)
                    print(f"Account deleted. Refund amount: {refund_amount}. Returning to main menu...")
                    return
                else:
                    print("Account deletion canceled. Returning to main menu...")
                    return
        print("Invalid username or password. Returning to main menu...")