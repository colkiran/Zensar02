
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index02.html", username=name, content="For Loop.....")

if __name__ == '__main__':
    app.run(debug=True)
