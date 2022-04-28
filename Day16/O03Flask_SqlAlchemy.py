
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello world"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///students.sqlite3'

# mysql+pymysql://root:@localhost/students

db = SQLAlchemy(app)

class Students(db.Model):
    studid = db.Column('student_id', db.Integer, primary_key=True)
    sname = db.Column(db.String(50))
    stdcls = db.Column(db.String(50))
    city = db.Column(db.String(50))


    def __init__(self, sname, scls, city):
        self.sname = sname
        self.stdcls = scls
        self.city = city

@app.route("/")
def show_all():
    return render_template("show_all.html", students = Students.query.all())

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['sname'] or not request.form['scls'] or not request.form['city']:
            flash("Please enter all the fields", "error")
        else:
            student = Students(request.form['sname'], request.form ['scls'], request.form['city'])
            db.session.add(student)
            db.session.commit()

            flash("Record added successfully into the database.......")
            return redirect(url_for("show_all"))
    return render_template("new.html")

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)





