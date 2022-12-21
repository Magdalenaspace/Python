class User:
    pass

# we'll fill this in shortly


# how we create a new instance of our class:
michael = User()
anna = User()

# Attributes: Characteristics shared by all instances of the class type.
# Methods: Actions that an object can perform. A user in a banking application, for example, may need to be able to calculate age based on the user's birthday or open a new bank account associated with that user.

#  constructor is a function that contains instructions for making a new instance of a class,

# __init__ method. - this method will designate some space in memory to store the user, and then assign the first name, last name and age by executing the lines below:

# declare a class and give it name User
class User:	
    # CONSTRUCTOR FUNCTION ______ creates the instance of the obejct	
    def __init__(self):  # <- representation of the object not the class
        #self is a placeholder for future instances, future users, like a blank form.
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

#__________constructor is a function that contains instructions for making a new instance of a class


# Making Instances orinak
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada #  accessing  with dot-notation: 



user_2 = User()
print(user_2.first_name) # also prints Ada


# declare a class and give it name Shoe
# class Shoe:		
#     def __init__(self):
#         self.brand = "Vans"
#         self.type = "Classic Sk8-Hi"
#     	self.price = 69.99
#     	self.in_stock = True


# skater_shoe = Shoe()
# dress_shoe = Shoe()
# # Accessing the instance's attributes
# print(skater_shoe.type) # Classic Sk8-Hi
# print(dress_shoe.type)	# Classic Sk8-Hi

# skater_shoe.type = "Low-top Trainers"
# print(skater_shoe.type)
# # output: Low-top Trainers
# dress_shoe.type = "Ballet Flats"
# print(dress_shoe.type)
# # output: Ballet Flats

# # Passing in Arguments

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand # self is like I AM a brans..... I AM type ,......
        self.type = shoe_type
        self.price = price
    	# the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats


# Much better!

#exercise

nike_shoe = Shoe("Nike", "sport shoe", 70.99)
nike_shoe.in_stock = False
print(nike_shoe.type)
# Update the in_stock attribute to False



# Methods & Updating Attributes





# Methods
# methods must be called from an instance of a class. 



class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")
# the first parameter of every method within a class should be self

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie

adrien.greeting()

# implicit passage of self. When we call on a method from an instance, the memory address of that instance, along with all of its information (name, email, balance), is passed in as self.

# SELF
# Параметр self включает в себя всю информацию об отдельном объекте, вызвавшем метод.
# метода __init__, он требует 3 аргумента.Однако, когда мы вызываем его, мы проходим только через два.


#  implicit passage of self. = calling on the method from the instance.
# Когда мы вызываем метод из экземпляра, адрес памяти этого экземпляра вместе со всей его информацией (имя, адрес электронной почты, баланс) передается как self.