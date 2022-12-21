# import statements, maybe some other routes
from flask import Flask, render_templates


# Create a new instance of the Flask class called "app"
app = Flask(__name__)  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return "Dojo!"

# for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = 'Sorry! No response. Try again.'
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html", banana = banana, num = num)


if __name__ =="__main__":
    app.run(debug=True) 
# should be the very last statement!




