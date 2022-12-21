class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

#Let's say you were receiving data from an external source like a data base, and wanted to turn this dictionary data into a Player object so you could write some useful methods associated with players. You can imagine just from the way the dictionary is structured that you might write your class like this:

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward -------=> constructor method
#constroctor method:  uniform way to always include that data whenever a user is created.
#function that contains instructions for making a new instance of a class
#used to initialize the instance members of the class.

#Now you have a Player object, that you can write methods for! You can also make more player instances if you have more data that comes back in that format.