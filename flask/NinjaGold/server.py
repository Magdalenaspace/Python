from flask import Flask, render_template, request, redirect, session
# from termcolor import colored, cprint
import random
import datetime

app = Flask(__name__)

app.secret_key = 'let it be'


@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    else:
        session["gold"] = session["gold"]
    return render_template("index.html", gold=session["gold"])


@app.route('/process_money', methods=["POST"])
def money():
    if "message" not in session:
        session["message"] = []

    if request.form['building'] == 'farm':
        session["earn"] = random.randrange(10,20)
        session["gold"] += session["earn"]
        session["message"].append("Earned "+ str(session["earn"])+ " gold from the farm!    " + str(datetime.datetime.now()))
        return redirect("/")


    elif request.form['building'] == 'cave':
        session["earn"] = random.randrange(5,10)
        session["gold"] += session["earn"]
        session["message"].append("Earned "+ str(session["earn"])+ " gold from the cave! " + str(datetime.datetime.now()))
        return redirect("/")

    elif request.form['building'] == 'house':
        session["earn"] = random.randrange(2,5)
        session["gold"] += session["earn"]
        session["message"].append("Earned "+ str(session["earn"])+ " gold from the house! " + str(datetime.datetime.now()))
        return redirect("/")

    elif request.form['building'] == 'casino':
        session["earn"] = random.randrange(-50,50)
        session["gold"] += session["earn"]
        if session["earn"] > 0:
            session['message'].append("Earned " + str(session["earn"])+ " gold from the farm! " + str(datetime.datetime.now()))
        else:
            session['message'].append("Lost " + str(session["earn"])+ " gold from the casino! " + str(datetime.datetime.now())) 

    if session["earn"] > 0:
       "message" = (session["message"],"red")
        # colored(session["message"],'red') # come back on adding colored lines on output
    else:
        session["message"] = colored('red')


        return redirect("/")      


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'




if __name__ =='__main__':
    app.run(debug=True, port=5001)
