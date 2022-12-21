from flask_app import app
from flask_app.controllers import users, messages


@app.route('/', defaults={'path': ''}) 
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'


if __name__ =='__main__':
    app.run(debug=True, port=5000)