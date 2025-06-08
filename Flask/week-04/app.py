from flask import Flask, session, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def login():
    if "user" in session:
        return render_template("welcome.html", name = session.get("user"))
    else:
        return render_template("login.html")

@app.route('/submit', methods=['POST'])
def welcome():
    username = request.form.get("username")
    password = request.form.get("password")

    userDatabase = {
        'admin' : '1234',
        'aaditya' : 'password',
        'satyam' : 'sattu1234',
        'aryan' : 'cp1234'
    }

    if username in userDatabase and password == userDatabase[username]:
        session['user'] = username
        return render_template("welcome.html", name = session.get("user"))
    return render_template("error.html")

@app.route('/logout')
def logout():
    session.pop("user", None)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)