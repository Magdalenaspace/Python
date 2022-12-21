from bank_account import BankAccount
#inheritance
# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     def deposit(self, amount):
#     pass
#     def withdraw(self, amount):
#     pass
#     def write_check(self, amount):
#     pass
#     def display_account_info(self):
#     pass
class CheckingAccount(BankAccount):
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# both the CheckingAccount and RetirementAccount classes both have all the attributes and functionality of the parent class

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	
        

    def withdraw(self, amount, is_early):
        if is_early:
    	    amount = amount * 1.10
        super().withdraw(amount)
        return self




# class RetirementAccount:
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth
#     def deposit(self, amount):
#     pass	# code - assess tax if necessary
#     def withdraw(self, amount):
#     pass	# code - assess penalty if necessary
#     def display_account_info(self):
#     pass	# code
    

