from player_list import players

class Player:
    def __init__(self, players):
        self.name = players["name"]
        self.age = players["age"]
        self.position = players["position"]
        self.team = players["team"]

# Player instances from a list of dictionaries
    @classmethod
    def add_players(cls,players):
        new_team = []
        for player in players:
            new_team.append(cls(player)) 
        return new_team

# __repr__(self) is a python system method that 
    # tells python how to handle representing that class 
    # when, for example the object is printed to the terminal.
    def __repr__(self):
        display = f"Player: name: {self.name}, \n age: {self.age},\n position: {self.position},\n team: {self.team}"
        return display
        
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward",
    "team": "Brooklyn Nets",
}

jason = {
    "name": "Jason Tatum",
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets",
}
    
# Create your Player instances here!
josh = {
    "name": "Kyrie Josh", 
    "age":22,
    "position": "extra", 
    "team": "Brooklyn Nets",
    }

# Player instances from a list of dictionaries
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
player_josh = Player(josh)

print(player_jason)
print("_"*68)
print(player_kyrie)
print("_"*68)
print(player_josh)
print("_"*68)
print(Player.add_players(players))

