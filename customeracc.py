
class CustomerAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_activated = False
        self.balance = 0