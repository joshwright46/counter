from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'secret_key' 

@app.route('/')
def index():

    if 'count' not in session:
        session["count"] = 0
    else:
        session["count"]+=1

    if 'views' not in session:
        session["views"] = 0
    else:
        session["views"] += 1

    return render_template("index.html", counter = int(session["count"]), viewed = int(session["views"]))

@app.route('/destroy_session')
def destroy():
    session["count"] = 0

    return redirect('/')

@app.route('/add_2')
def add_2():
    session["count"] += 1
    return redirect('/')

@app.route('/add_this', methods=['POST'])
def add_this():
    
    number_from_form = request.form['number']

    if number_from_form == '':
        session["count"] += -1
    else:
        session["count"] += (int(number_from_form) - 1)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)