
from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Secretkey"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("index04.html", uname="Mike Tyson")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user", usr="user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/users")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h2> Welcome {user}</h2>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)