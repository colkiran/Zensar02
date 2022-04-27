

from flask import Flask, redirect, url_for

app = Flask(__name__)                   #  __main__

@app.route("/")
def fun():
    return "<h1> Hello World </h1>"

@app.route("/<username>")
def user(username):
    return f"<h2> Greetings  Mr.{username}, Welcome to the event.... </h2>"

@app.route("/admin")
def admin():
    return redirect(url_for("user", username="Root"))

# disabled the debug mode   -   any changes to the code - will not reflect in the browser (need to restart)
if __name__ == '__main__':
    app.run()