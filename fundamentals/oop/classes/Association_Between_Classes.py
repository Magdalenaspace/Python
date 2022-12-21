class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            "Insufficient Funds: Charging a $5 fee"
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += {self.balance * self.rate}
            return self

@classmethod
def print_all_accounts(cls):
    for account in cls.account:
        account.display_account_info()
        

class User: #class attribute 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line


    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)


