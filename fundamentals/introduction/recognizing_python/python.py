num1 = 42 #variable declaration, number initialized
num2 = 2.3 #float initialized
boolean = True #boolean initialized
string = 'Hello World' #string initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
#list initialized []
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#dictionary initialized {}
fruit = ('blueberry', 'strawberry', 'banana')
#tuple initialized () immutable list, objects (form data from front end to back end) 

print(type(fruit)) #type check 
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') 
print(person['name']) #lis add value
person['name'] = 'George' # dictionary access value
person['eye_color'] = 'blue' #dictionary change value
print(fruit[2]) # access tuple data

if num1 > 45: #conditional if , evaluation, print to console ,conditional els, print to console 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditional if, elif, else, print console 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop, starts at 0 goes up to 5
    print(x)
for x in range(2,5):#starts at 2 goes up to 5
    print(x)
for x in range(2,10,3): #starts at 2 goes up until 10 increments  by 3 
    print(x)
x = 0
while(x < 5): #while loop, printing to console, incrementing X
    print(x)
    x += 1

pizza_toppings.pop() # List delete value at end
pizza_toppings.pop(1) # List delete value at index

print(person) # print console
person.pop('eye_color') # dictionary delete value 
print(person) # print console dictionary

for topping in pizza_toppings: # for loop through the list
    if topping == 'Pepperoni': # conditional if 
        continue #continues
    print('After 1st if statement') #print_hello_x_times
    if topping == 'Olives':
        break  #stops the loop 

def print_hello_ten_times():# function deceleration
    for num in range(10): #for loop starts at 0 goes util 10
        print('Hello') # prints in console 

print_hello_ten_times() # function call

def print_hello_x_times(x): # function deceleration with parameter x
    for num in range(x):   #for loop starts at 0 goes util x(4 )
        print('Hello') # prints to console

print_hello_x_times(4) # function call

def print_hello_x_or_ten_times(x = 10): # function deceleration with (named)default parameter
    for num in range(x): # foe loop until x
        print('Hello') # print to console 

print_hello_x_or_ten_times() #function call goes to 10(default)
print_hello_x_or_ten_times(4) # #function call goes to 4 (overriding)


"""
Bonus section
"""

# print(num3)                       # prints to console 
# num3 = 72                         # NameError
# fruit[0] = 'cranberry'            # TypeError
# print(person['favorite_team'])    # KeyError (favorite_team does not exist in {})
# print(pizza_toppings[7])          # IndexError: List index out of range
#   print(boolean)                  # IndentationError: unexpected indent
# fruit.append('raspberry').        # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                      # AttributeError: 'tuple' object has no attribute 'pop'