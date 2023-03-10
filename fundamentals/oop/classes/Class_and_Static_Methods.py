# Methods that belong to the class and not the instance.
class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


# Changing them on the entire class:
BankAccount.bank_name = "Bank of Dojo"
    
print(adriensAccount.bank_name)
# output: Bank of Dojo
    
print(sadiesAccount.bank_name)
# output: Bank of Dojo

# Changing them on an instance:  
adriensAccount = BankAccount()
adriensAccount.bank_name = "Dojo Credit Union"
print(adriensAccount.bank_name)
# output: Dojo Credit Union

# @classmethod
class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum


# It's important to know that class methods have no access to the instance attribute or any attribute that starts with self.


# @staticmethod

# Static methods are functions defined within the class with a decorator @staticmethod.  They have no access on instance or class attributes, so if we need any existing values, they need to be passed in as arguments.

# If we wanted our BankAccount class to have a utility function to add or subtract we could implement @staticmethod on the class.

class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
            return False
        else:
            return True

# In Python, static methods offer us the opportunity to organize our code in a better way. We could do a simple check to see if the account can be withdrawn from, but what if we want to scale up our application with more logic around this idea? Well then we would have to update everywhere we are making that evaluation, but if we put it in a @staticmethod, then we can update all the checks from one place. And our code becomes a bit more D.R.Y.