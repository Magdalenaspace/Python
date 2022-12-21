
from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.controllers import cookie_orders


@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'


if __name__ =='__main__':
    app.run(debug=True)
