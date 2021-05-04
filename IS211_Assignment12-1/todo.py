from flask import Flask, render_template, request, redirect, session
from flask import g
app = Flask(__name__)
import sqlite3 as lite
import logging
from logging import FileHandler
file_handler = FileHandler("teacher_file.log")
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.debug = True

def get_db():
    if 'db' not in g:
        g.db = lite.connect('C:/Users/batsh/Documents/IS 211/IS211_Assignment12/week12database.db')

    return g.db

@app.route('/')
def hello_world():
    app.logger.error("This is a custom error message!")
    author = "Me"
    name = "teacher"

    if 'username' in session:
        user = session['username']
    else:
        user = " "


    quizzes_info = {}
    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute("SELECT* FROM quizzes")
        rows = cur.fetchall()
        for row in rows:
            quizzes_info[row[1]] = row[0]

    students_info = {}
    with db:
        cur = db.cursor()
        cur.execute("SELECT* FROM students")
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
            students_info[row[1]] = row[0]
        print(students_info)
    return render_template('form.html', author=author, name=name, quiz_info=quizzes_info, student_info=students_info, user=user)

@app.route('/enter_user', methods=['POST'])
def signup():
    user = request.form['user']
    Array = []
    Array.append(user)
    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute(" INSERT into users (name_authorized) values(?);", Array)
    print("The current user is '" + user + "'")
    db.commit()
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login():
    user = request.form['user']
    Array = []
    Array.append(user)
    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute(" SELECT* FROM users ")
        rows = cur.fetchall()
        # print(rows)
        for row in rows:
            if user == row[1]:
                session['username'] = user
            print(row)

    print("The current user is '" + user + "'")
    db.commit()
    return redirect('/')




@app.route('/submit_student', methods=['POST'])
def if_authorized():
    student = request.form['student']
    Array = []
    Array.append(student)

    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute(" INSERT into students (name) values(?);", Array)
    print("The student added was '" + student + "'")
    db.commit()
    return redirect('/')


@app.route('/submit_quiz', methods=['POST'])
def quiz():
    quiz_name = request.form['quiz']
    q_Array = []
    q_Array.append(quiz_name)

    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute(" INSERT into quizzes (quiz_name) values(?)", q_Array)
    print("The quiz name added was '" + quiz_name + "'")
    cur.close()
    return redirect('/')

@app.route('/submit_score', methods=['POST'])
def score_results():
    graded_score = request.form['score']
    id_quiz = request.form['q_id']
    id_students = request.form['s_id']

    s_Array = []
    s_Array.append(graded_score)
    s_Array.append(id_students)
    s_Array.append(id_quiz)
    s_Array.append(1)


    db = get_db()
    with db:
        cur = db.cursor()
        cur.execute(" INSERT into scores (score, student_id, quiz_id , user_id) values(?,?,?,?)", s_Array)
    print("The score added was '" + graded_score + "'")
    cur.close()
    return redirect('/')



if __name__ == "__main__":
    app.run()
