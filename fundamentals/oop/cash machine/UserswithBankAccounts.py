class User:
    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}

    def open_new_account(self, with_amount=0, interest=0.04, account_type="checking"):
        print("Creating new account..")
        self.accounts[account_type] = BankAccount(with_amount, interest, account_type)
        return self

    def display_user_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self
    
    def make_withdrawal(self, amount, account_type = "checking"):
        self.accounts[account_type].withdrawal(amount) 
        return self

    # have this method decrease the user's balance by the amount and add that amount 
    def transfer_money(self, other_user, other_user_account_type, amount, from_account_type):
        if self.accounts[from_account_type].balance < amount:
            print("Insufficient funds")
            return self
        print("Transferring $" + str(amount) + " into " + other_user.name + "'s " + other_user_account_type + " account." )

        self.accounts[from_account_type].balance -= amount
        other_user.accounts[other_user_account_type].balance += amount
        
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
    bank_name = "Chase"
    all_accounts = []

    def __init__(self, balance=0, interest=0.4, account_type="chekiang"):
        self.account_type = account_type
        self.balance = balance
        self.interest_rate = interest
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account: ", self.account_type)
        print("Account Balance: $" + str(self.balance))
        print("Interest rate", self.interest_rate)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        print("Yielding Interest:", self.balance)
        return self

    # class method to get balance of all accounts
    @classmethod #cls= BankAccount
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return cls
    
    #? class method to get balance of all accounts
    @classmethod
    def print_all(cls):  
        for account in cls.all_accounts:
            account.display_account_info()
        return cls


she = User("Kat")
she.open_new_account(0, 0.05).display_user_balance().make_deposit(100)
she.make_deposit(300).display_user_balance() 
she.open_new_account(500, 0, "savings")
she.display_user_balance()

print("*"*30)

he  = User("Tom")
he.open_new_account().make_deposit(700)
he.display_user_balance()
he.transfer_money(she, "savings", 300, "checking")
he.display_user_balance()

print("*"*30)
print("BANK INFO ALL ACCOUNTS")
print("-"*30)
print(BankAccount.print_all().all_balances())

print("*"*30)

    
