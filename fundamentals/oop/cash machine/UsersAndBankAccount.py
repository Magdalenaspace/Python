class User:

    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}

    def open_new_account(self, with_amount=0, interest=0.04, account_type="checking"):
        print("Creating new account..")
        self.accounts[account_type] = BankAccount(with_amount, interest, account_type)
        return self

    # have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount, account_type="checking"):
        self.accounts[account_type].withdraw(amount)
        return self

    # have this method print the user's name and account balance to the terminal
    # eg. User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self

    # have this method decrease the user's balance by the amount and add that amount 
    def transfer_money(self, other_user, other_user_acc_type, amount, from_account_type):
        if self.accounts[from_account_type].balance < amount:
            print("Insufficient funds")
            return self
        print("Transferring $" + str(amount) + " into " + other_user.name + "'s " + other_user_acc_type + " account.")
        self.accounts[from_account_type].balance -= amount
        other_user.accounts[other_user_acc_type].balance += amount

        self.display_user_balance()
        other_user.display_user_balance()

        return self

    def make_deposit(self, amount, account_type="checking"):
        self.accounts[account_type].deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:

    bank_name = "First National Dojo"
    all_accounts = []


    def __init__(self, balance=0, interest=0.04, account_type="checking"):
        self.balance = balance
        self.interest_rate = interest
        self.account_type = account_type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account: ", self.account_type)
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self

    def yield_interest(self):
        print("Yielding interest...")
        self.balance += self.balance * self.interest_rate
        return self
    
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls


# User test
sadie = User("Sadie Sink")
sadie.open_new_account(0, 0.05)
sadie.make_deposit(100).display_user_balance()
sadie.open_new_account(500, 0, "savings")

sami = User("Samantha Bee")
sami.open_new_account(300, 0.045).display_user_balance()
sami.transfer_money(sadie, "checking", 100, "checking").make_withdrawal(150).display_user_balance()
print("*"*15)
print("BANK INFO ALL ACCOUNTS")
print("*"*15)
print(BankAccount.print_all().all_balances())

print("*"*15)
print("Making Transfers")
print("*"*15)
sadie.make_deposit(100,"savings").display_user_balance()
sadie.transfer_money(sadie, "checking", 50, "savings").display_user_balance()

sadie.transfer_money(sami, "checking", 100, "savings")

print("*"*15)
print("BANK INFO ALL ACCOUNTS")
print("*"*15)
print(BankAccount.print_all().all_balances())



# b = BankAccount(interest=0.04)
# b.withdraw(5)
# b.deposit(10)
# b.display_account_info()
# b.deposit(20)
# b.display_account_info()
# b.withdraw(3)
# b.display_account_info()
# b.yield_interest()
# b.display_account_info()