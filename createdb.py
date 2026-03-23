import sqlite3

conn = sqlite3.connect('results.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    roll_number TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
)
''')

# Create marks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS marks (
    mark_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT NOT NULL,
    marks INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

# Insert dummy data
students = [
    ('101', 'Alice Johnson'),
    ('102', 'Bob Smith'),
    ('103', 'Charlie Lee')
]
cursor.executemany('INSERT INTO students (roll_number, name) VALUES (?, ?)', students)

marks = [
    (1, 'Mathematics', 95),
    (1, 'Physics', 88),
    (1, 'Chemistry', 92),
    (2, 'Mathematics', 78),
    (2, 'Physics', 85),
    (2, 'Chemistry', 80),
    (3, 'Mathematics', 65),
    (3, 'Physics', 72),
    (3, 'Chemistry', 70)
]
cursor.executemany('INSERT INTO marks (student_id, subject, marks) VALUES (?, ?, ?)', marks)

conn.commit()
conn.close()

print("Database 'results.db' created successfully.")
