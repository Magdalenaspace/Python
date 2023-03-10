from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping
# Creating a circular import, which is bad and breaks our code.
from flask import flash

from flask_app.models import topping
class Burger:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated']
        # We now create a list so that later we can add in all the topping objects that relate to a burger.
        self.toppings = []
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"

        result = connectToMySQL('burgers').query_db(query)
        burgers = []

        for u in result:
            burgers.append(cls(u))
        return burgers
        
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO burgers ( name, bun, meat, calories,  created_at , updated_at, retuarant_id ) VALUES (%(name)s, %(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db( query, data)

    # This method will retrieve the burger with all the toppings that are associated with the burger.
    @classmethod
    def get_burger_with_toppings( cls , data ):
        query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        burger = cls( results[0] )
        for row_from_db in results:
        # Now we parse the topping data to make instances of toppings and add them into our list.
            topping_data = {
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["topping_name"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger

    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid