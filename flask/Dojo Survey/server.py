from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'time'
# Have the root route ("/") show a page with the form
@app.route('/')
def  index():
    return render_template("index.html")

# Put the form data into session
@app.route("/input", methods=['POST'])
def input():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/results')

@app.route("/results")
def results():
    return render_template('results.html')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')



@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'

if __name__=="__main__":
    app.run(debug=True, port=5001)