from flask import Flask, redirect, render_template, request, Response, url_for, session

# Creating Flask Object
app = Flask(__name__)
app.secret_key = "supersecret"

# Home Page
@app.route('/')
def home():
    if "user" in session:
        return render_template("success.html", user=session.get("user"))
    return render_template("form.html")

# Login Route
@app.route('/submit', methods=["POST"])
def submit():
    username = request.form.get("username")
    password  = request.form.get("password")

    if username == "admin" and password == "1234":
        session["user"] = username
        return render_template("success.html", user = session.get("user"))
    return render_template('error.html')

# Lgout Route
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
