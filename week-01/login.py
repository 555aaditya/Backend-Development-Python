from flask import Flask, request, Response, redirect, url_for, session

# Creating Flask App Object
app = Flask(__name__)
app.secret_key = "supersecret"

# Home Page
@app.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            # store user data in session
            session["user"] = username
            return redirect(url_for("welcome"))
        
        else:
            return Response("Invalid Credentials", mimetype="text/plain")
    
    return '''
            <h2>Login Page</h2>
            <form method="POST">
                Username: <input type="text" name="username"><br>
                Password: <input type="text" name="password"><br>
            <input type="submit" value="login">
            </form>
    '''

# welcome page after login
@app.route('/welcome')
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}</h2>
        <a href={url_for('logout')}>Logout</a>
    '''
    return redirect(url_for("login"))

# log out route
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)