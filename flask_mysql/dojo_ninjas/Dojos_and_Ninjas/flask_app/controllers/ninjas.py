from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html',dojos=Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')

@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data ={
        "id":id
    }
    return render_template("edit.html",ninja=Ninja.get_one(data))


@app.route('/ninja/update', methods=['POST'])
def update():
    dojo_id = request.form['dojo_id']
    Ninja.update(request.form)
    return redirect(f"/dojo/{dojo_id}")

@app.route('/ninja/delete/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Ninja.destroy(data)
    return redirect('/dojos')
