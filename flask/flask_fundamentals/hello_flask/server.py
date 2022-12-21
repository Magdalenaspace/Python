from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/hello/<string:banana>/<int:num>')          # The "@" decorator associates this route with the function immediately following
# def hello(banana,num):
#     return render_template("hello.html",banana=banana,num=num)

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id



# @app.route('/success')
# def success():
#     return "success"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)    # Run the app in debug mode.

# Notice how we are accessing the app object and running the route method, passing in a string that is the route that we want to add to our application. You must do this for every route that you want to add to our application.
# import statements, maybe some other routes
    
# @app.route('/success')
# def success():
#     return "success"
        
# app.run(debug=True) should be the very last statement! 

