class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

        # implement the following methods:
        # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
            self.pet.play()
            return self

        # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) == 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        elif len(self.treats) > 0:
            food = self.treats[0]
            print(f"Good my girl {self.pet.name}, here is your {food} my love!")
            self.pet.eat()
        else:
            print("You need more pet food my love!")
            return self

        # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
            self.pet.noise().play()


class Pet:
        def __init__(self,name , type , tricks, noise ):
            self.name = name
            self.type = type
            self.tricks = tricks
            self.health = 100
            self.energy = 100
            self.noise = noise

    # implement the following methods:
    # sleep() - increases the pets energy by 25
        def sleep(self):
            self.energy += 22
            return self
    # eat() - increases the pet's energy by 5 & health by 10
        def eat(self):
            self.health +=10
            self.energy += 15
            return self
    # play() - increases the pet's health by 5
        def play(self):
            self.health += 50
            self.energy -= 22 
            return self
    # noise() - prints out the pet's sound
        def noise(self):
            input(self.noise)
            return self

my_treats = ['banana', 'eggs', 'trash']
my_pet_food = ['Pizza','Burger']

faust = Pet("Faust", "dog", "lives like a human", "i love yoo" )
maggie = Ninja("Magdalena", "S", my_treats, my_pet_food, faust)


faust.eat()
maggie.feed()
