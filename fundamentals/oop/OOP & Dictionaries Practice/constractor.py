class Player:
    def __init__(self, them): 
        self.name = them['name'] # its in 
        self.age = them['age'] 
        self.position = them['position'] 
        self.team = them['team'] 

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

nelly = {"name": "Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
player_kevin = Player(kevin)
player_nelly = Player(nelly)