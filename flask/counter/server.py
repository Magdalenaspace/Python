from flask import Flask, render_template, redirect, session

app = Flask(__name__)

app.secret_key = 'time'

@app.route('/')
def clicked():
    if 'clicked' in session:
            session['clicked'] += 1
    else:
            session['clicked'] = 0
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()		# clears all keys
    # session.pop('clicked')		# clears a specific key
    return redirect('/')


@app.route('/', defaults={'path': ''}) #to secure the browser
@app.route('/<path:path>')
def catch_all(path):
    return 'invalid URL'

if __name__ =='__main__':
    app.run(debug=True, port=5001)
