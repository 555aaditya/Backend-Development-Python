from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        feedback = request.form.get("feedback")
        print(request.method)
        return render_template("thanks.html", name=name, feedback=feedback)

    else:
        print(request.method)
        return render_template("feedback.html")
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)