import sqlite3

def create_tables():
    conn = sqlite3.connect('hw13.db')

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT NULL, first_name TEXT NULL, last_name TEXT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS quizzes(id INTEGER PRIMARY KEY AUTOINCREMENT NULL, subject TEXT NULL, quiz_questions INTEGER NULL, date DATE NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS student_quiz_results(id INTEGER PRIMARY KEY AUTOINCREMENT NULL, student_first_name TEXT NULL,student_last_name TEXT NULL)")

    conn.commit()
    conn.close()




if __name__ =="__main__":
    create_tables()