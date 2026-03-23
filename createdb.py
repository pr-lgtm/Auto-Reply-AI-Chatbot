import sqlite3

def main():
    #Connect to database (Creates it if missing)
    conn= sqlite3.connect("results.db")
    cursor= conn.cursor()

    #Create Tables
    cursor.execute(""" CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   roll_number INTEGER UNIQUE NOT NULL)
                   """)
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS marks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   subject TEXT NOT NULL,
                   score INTEGER NOT NULL,
                   FOREIGN KEY(student_id) REFERENCES students(id)
                   )
                   """)
    #Insert Dummy Students
    students=[("Priyanshu",5025),("Rahul",101),("Amit",102)]
    for name, roll in students:
        cursor.execute("INSERT OR IGNORE INTO students (name, roll_number) VALUES (?, ?)", (name, roll))

    #Insert Dummy Marks
    #Clear old data first to avoid duplicates
    cursor.execute("DELETE FROM marks")

    #GEt student IDs
    cursor.execute("SELECT id,roll_number FROM students")
    for student_id, roll in cursor.fetchall():
        if roll == 5025: #Your marks
            data = [("Python",95),("Statistics",88),("Math",92),("English",85)]
        else: #Other students' marks
            data = [("Python",70),("Statistics",60),("Math",75),("English",80)]
        for subject, score in data:
            cursor.execute("INSERT INTO marks (student_id, subject, score) VALUES (?,?, ?)",(student_id,subject,score))
    conn.commit()
    conn.close()
    print("Database 'results.db' created successfully.")

if __name__ == "__main__":
    main()
