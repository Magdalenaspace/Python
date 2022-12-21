from flask import render_template,redirect,request,session 

from flask_app import app
# ...server.py

from flask_app.models.burger import Burger

@app.route('/')
def index():
    return render_template("index.html")

# before transfering the data into data object and saving in database it needs to be checked
@app.route('/create',methods=['POST'])
def create():
    if not Burger.validate_burger(request.form):
        return redirect('/')
        # if it comes false we are redirecting to the rout that burger form  is  and thats the index route in this case
        # that index HTML shuld be able to render those messages but we need tu write code with 7 lines

    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')




@app.route('/burgers')
def burgers():
    return render_template("results.html",all_burgers=Burger.get_all())

@app.route('/create/burger',methods=['POST'])
def create_burger():
	data = {
        "name" : request.form['name'],
        "bun" : request.form['bun'],
        "meat" : request.form['meat'],
        "calories" : request.form['calories']
	}
	Burger.save(data)
	return redirect('/burgers')


    
@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html",burger=Burger.get_one(data))

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger = Burger.get_one(data))

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')