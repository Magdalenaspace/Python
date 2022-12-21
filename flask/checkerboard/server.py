from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display():
    return render_template("index.html", row=8, col=8, color_one="black", color_two="white")

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color_one="black", color_two="white")

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html", row=x, col=y, color_one="black", color_two="white")

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_or(x,y,one,two):
    return render_template("index.html",row=x,col=y,color_one=one, color_two=two)

@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'


if __name__ == "__main__":  
    app.run(debug=True)