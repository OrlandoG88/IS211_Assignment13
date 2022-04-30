from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw13.db'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Quizzes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    num = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)

    def __init__(self, subject, num, date):
        self.subject = subject
        self.num = num
        self.date = date


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String, nullable=False)
    quiz = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, student, quiz, score):
        self.student = student
        self.quiz = quiz
        self.score = score


@app.route('/', methods=['POST', 'GET'])
def index():
        return render_template("index.html",)

@app.route('/Dashboard', methods=['POST', 'GET'])
def dashboard():
    students = Students.query.order_by(Students.id)
    quizzes = Quizzes.query.order_by(Quizzes.id)
    scores = Scores.query.order_by(Scores.id)
    return render_template("Dashboard.html", students=students, quizzes=quizzes, scores=scores)


@app.route('/AddStudent', methods=['POST', 'GET'])
def AddStudent():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        new_student = Students(first_name=first_name, last_name=last_name)
        db.session.add(new_student)
        db.session.commit()
        return redirect('/AddStudent')
    else:
        return render_template("AddStudent.html",)


@app.route('/addQuiz', methods=['POST', 'GET'])
def addQuiz():
    if request.method == 'POST':
        subject = request.form['subject']
        num = request.form['num']
        date = request.form['date']
        new_quiz = Quizzes(subject=subject, num=num, date=date)
        db.session.add(new_quiz)
        db.session.commit()
        return redirect('/addQuiz')
    else:
        return render_template("addQuiz.html",)


@app.route('/Addresults', methods=['POST', 'GET'])
def Addresults():
    if request.method == 'POST':
        student = request.form['student']
        quiz = request.form['quiz']
        score = request.form['score']
        new_grade = Scores(student=student, quiz=quiz, score=score)
        db.session.add(new_grade)
        db.session.commit()
        return redirect('/Addresults')
    else:
        students = Students.query.order_by(Students.id)
        quizzes = Quizzes.query.order_by(Quizzes.id)
        return render_template("Addresults.html", students=students, quizzes=quizzes)


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)