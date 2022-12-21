from flask import Flask
app = Flask(__name__)

app.secret_key = "meh"

from flask_app.controllers import cookie_orders
