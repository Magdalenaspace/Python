from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data["dojo_id"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojo_ninjas').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL("dojo_ninjas").query_db(query)
        ninjas = []
        for nin in result:
            ninjas.append(cls(nin))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL('dojo_ninjas').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name= %(first_name)s, last_name=%(last_name)s, age=%(age)s,created_at=NOW(),updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninjas').query_db(query,data)
        
    
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninjas').query_db(query,data)

    