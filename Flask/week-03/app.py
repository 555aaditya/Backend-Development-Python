from flask import Flask, render_template, request, url_for  

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/submit', methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    userDatabase = {
        'admin' : '1234',
        'aaditya' : 'password',
        'satyam' : 'sattu',
        'aryan' : 'cp123'
    }

    if username in userDatabase and password == userDatabase[username]:
        return render_template("welcome.html", name=username)
    else:
        return render_template("error.html")
    
if __name__ == '__main__':
    app.run(port='4444', host='0.0.0.0', debug=False)