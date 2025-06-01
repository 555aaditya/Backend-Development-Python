# Import Flask
from flask import Flask, request

# Flask Object with name app specifying main file
app = Flask(__name__)

# Route Decorator
@app.route('/')
def home():
    return "Hello World"

# Using HTTP Methods
@app.route('/submit', methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You sent data"
    else:
        return "You are viewing the form"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
