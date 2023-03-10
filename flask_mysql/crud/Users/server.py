from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

app.secret_key = ''


@app.route('/')
def index():
    return redirect('/users')



@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("create.html")


@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')



@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'




if __name__ =='__main__':
    app.run(debug=True, port = 5001)