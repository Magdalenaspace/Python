from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models import post
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)

    if not is_valid:
    # User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    #putting user id in session
    return redirect('/wall')


@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/wall')


@app.route('/wall')
def dashboard():
    if 'user_id' in session:
        return render_template("wall.html",
        current_user = User.get_by_id({'id': session['user_id']})
        ,all_posts = post.Post.get_all())
    return redirect('/')
    


    # data ={
    #     'id': session['user_id']
    # }
    # user = User.get_one(data)
    # posts = Post.get_user_posts(data)
    # users = User.get_all()
    # (user=user,users=users,posts=posts))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')