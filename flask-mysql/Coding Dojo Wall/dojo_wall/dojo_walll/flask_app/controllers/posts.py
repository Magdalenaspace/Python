from flask import render_template, session,flash,redirect, request
from flask_app import app
from flask_app.models import user
from flask_app.models import post

# app.route('/hello')
# def hello():
#     return hello

@app.route('/create', methods=['POST'])
def post_a_post():
    print(request.form)
    if post.Post.validate_post(request.form):
        data = { 
            'content': request.form['content'],
            'user_id': session['user_id']
        }
        id = post.Post.save(data)
        return redirect('/wall')
    #putting user id in session
    return redirect('/wall')



@app.route('/destroy/post/<id>')
def destroy_post(id):
    if 'user_id' in session:
        data ={
            'id': id
        }
        post.Post.destroy(data)
        return redirect('/wall')
    return redirect('/')



# # needed routed display, edit,