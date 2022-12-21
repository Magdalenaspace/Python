from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from datetime import datetime
import math


class Post:
    db = 'dojoWall'
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.creator = None
        self.time = None

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['content']) < 1:
            flash("Can Not Be Blank!")
            is_valid=False     
        return is_valid

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO posts 
        (content, user_id) 
        VALUES (%(content)s,%(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)


    @classmethod
    def get_all(cls):
        query = """
        SELECT posts. *, 
        users.first_name as username 
        FROM posts JOIN users ON user_id = posts.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        output =[]
        for row in results:
            this_post = cls(row)
            this_post.time = Post.time_span(this_post.created_at)
            this_post.creator = row['username']
            output.append(this_post)
        return output

    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    @staticmethod
    def time_span(time):
        now = datetime.now()
        delta = now - time
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"