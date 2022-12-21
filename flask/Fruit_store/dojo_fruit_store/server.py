from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)

    print('strawberry', request.form['strawberry'])
    print('raspberry', request.form['raspberry'])
    print('apple', request.form['apple'])
    print('blackberry', request.form['blackberry'])
    print('first_name', request.form['first_name'])
    print('last_name', request.form['last_name'])
    print('student_id', request.form['student_id'])
    print("-"*40)

    
    a=int(request.form['strawberry'])
    b=int(request.form['raspberry'])
    c=int(request.form['apple'])
    d=int(request.form['blackberry'])
    sum = a + b + c + d
    print(sum)
    import datetime
    
    dt = datetime.datetime.now().strftime("%B %d %X %p")
    return render_template("checkout.html", info = sum, timestamp = dt)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, port=5001)    