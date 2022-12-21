from flask import Flask, render_template
app = Flask(__name__)

app.secret_key="tea"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    if request.form['hidden_form'] == 'register':
        # do registration process

    elif request.form['hidden_form'] == 'login':
        # do login process
        




@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'




if __name__ =='__main__':
    app.run(debug=True)
