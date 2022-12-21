class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
# Create two shoe instances   <- this is being called in the global scope as the indentation is  shows so
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
        
# The skater shoes go on sale by 20% reduced price:
skater_shoe.price = skater_shoe.price * (1 - 0.2)
        
# The dress shoes go on sale by 10% reduction:
dress_shoe.price = dress_shoe.price * (1 - 0.1)
        
# The skater shoes go on sale AGAIN by another 10%:
skater_shoe.price = skater_shoe.price * (1 - 0.1)

# Look again at the last three lines of code. which exact parts of those lines were different, and which were the same?
# the ones that are the same is better to wrap in to the method so  we will not repeat ourselves.

# Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
      def on_sale_by_percent(self, percent_off): #<- self here is the shoes instance 
         self.price = self.price * (1-percent_off) # <- we put the method in global scope after class decleration


# # exercise
# class Shoe:
    
#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         self.in_stock = True
    
#     # Takes a float/percent as an argument and reduces the
#     # price of the item by that percentage.
#     def on_sale_by_percent(self, percent_off):
#         self.price = self.price * (1-percent_off)
    
#     # Returns a total with tax added to the price.
#     def total_with_tax(self, tax_rate):
#         tax = self.price * tax_rate
#         total = self.price + tax
#         return total
    
#     # Reduces the price by a fixed dollar amount.
#     def cut_price_by(self, amount):
#         if amount < self.price:
#             self.price -= amount
#         else:
#             print("Price deduction too large.")

# # Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
# my_shoe = Shoe("Converse", "Low-tops", 36.00)
# print(my_shoe.total_with_tax(0.05))
# my_shoe.cut_price_by(10)
# print(my_shoe.price)

# your_shoe = Shoe("adidas", "yeezy", 700)
# print(your_shoe.total_with_tax(0.05))
# print(your_shoe.brand)
# your_shoe.price = your_shoe.price *(1 - 0.02)
# print(your_shoe.total_with_tax(0.05))
