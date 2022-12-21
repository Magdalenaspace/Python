# modularizing/parent.py
local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
print(__name__) #impotrts parent in childe file
# print(locals())if __name__ == "__main__":

    product = Product([args])
    print(product)
    print(product.add_tax(0.18))




