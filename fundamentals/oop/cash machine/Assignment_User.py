class User:
    def __init__(self, fist_name, last_name, email, age):
        self.fist_name = fist_name
        self.last_name = last_name
        self.email = email 
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Fist Name: {self.fist_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        return self  # <- we do return statement for chaining


        
# spend_points(self, amount) - have this method decrease the user's points by the amount specified
    def  spend_points(self, amount):
        if self.gold_card_points <= amount:
            ("You are out of points.")
            return 
        self.gold_card_points -= amount
        return self 

# enroll(self) - Have this method change the user's member status to True.
def enroll(self): # we always need to check the first before any changes
    if self.is_rewards_member:
        print("User already is a member")
        return False
    
    self.is_rewards_member = True
    # Set their gold card points to 200.
    self.gold_card_points = 200    
    return self


user_is_female = User("Maggie",  "Samuel", "ms@gmail.com", "Females dont have an age.")
enroll(user_is_female) # <- we call enroll() this way, because the def is in a global scope(but it has to be in a local scope, and after display_info(), JUST TESTING) 
user_is_female.spend_points(50).display_info()
user_is_female.is_rewards_member

user_is_male = User("Josh", "Shwarts", "js@gmail.com", 26)
enroll(user_is_male).spend_points(80).display_info()

user_is_non_binary = User("Sand", "Man", "sm@gmail.com", 33)
enroll(user_is_non_binary)
user_is_non_binary.spend_points(40).display_info()



