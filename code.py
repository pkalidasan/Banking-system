class Bank:
    bankname = "ICICI Bank"
    branch = "kottayam branch"
    ifsc_code = "ICICI0075"
# class attributes
    def __init__(self, username, password,account_number):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.balance = 0.0

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawal successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Your account balance is : {self.balance}")

    print(f"Welcome to {bankname}")

# Create a bank account
account = Bank("Abin jose", "12345", account_number="98765")

# Customer Login id
username = input("Enter username: ")
password = input("Enter password: ")
account_number= input("enter the account number")

if account.login(username, password):
    print("Login successfully.")
else:
    print("Invalid username or password.")
    exit()

# Deposited Amount
amount_to_deposit = float(input("Enter amount to deposit: "))
account.deposit(amount_to_deposit)

# Withdrawal Amount
amount_to_withdraw = float(input("Enter amount to withdraw: "))
account.withdraw(amount_to_withdraw)

# checking balance
account.check_balance()





