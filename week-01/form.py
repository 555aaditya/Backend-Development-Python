from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def form():
    if "user" in session:
        return redirect(url_for("home"))
    return render_template("form.html")

@app.route('/submit', methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "123":
        session["user"] = username 
        return redirect(url_for('home'))
    return redirect(url_for('form'))

@app.route('/home')
def home():
    if "user" not in session:
        return redirect(url_for('form'))
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)