import sys
import sqlite3
from tabulate import tabulate

def main():
    """
    Main controller for the Result Chatbot.
    Connects to DB, authenticates user, and runs the chat loop.
    """
    try:
        conn= sqlite3.connect("results.db")
    except sqlite3.Error:
        sys.exit("Error: Could not find results.db.Please run create_db.py first.")

    print("---University Result System(CLI)---")

    #1. Authenticate User
    student_id, name= login(conn)
    print(f"\nWelcome, {name}!")
    print("I can answer queries like: 'My average', 'Total Marks', 'Percentage','Highest score','Minimum Marks', or 'Marks in [Subject]'.")
    print("Type 'exit' to quit.\n")

    #2. Main Chat Loop
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit","quit"]:
                print("Goodbye!")
                break

            #Generate response
            response= generate_response(conn, student_id, user_input)
            print(f"Bot: {response}\n")
        except (EOFError, KeyboardInterrupt):
            break

    conn.close()

def login(conn):
    """
    Prompts for Roll Number and verifies against DB.
    """
    cursor= conn.cursor()
    while True:
        roll= input("Enter Roll Number (e.g., 5025,101): ").strip()

        #Check database for this roll number
        cursor.execute("SELECT id, name FROM students WHERE roll_number = ?",(roll,))
        row= cursor.fetchone()

        if row:
            return row[0], row[1]
        else:
            print("Roll number not found.Please try again.")

def generate_response(conn, student_id, text):
    """
    Analyses text keywords using simple Python 'in' statements.
    """
    text= text.lower()
    cursor= conn.cursor()

    # 1. Query: AVERAGE
    #We check if any these simple words are in the user's text
    if "average" in text or "avg" in text or "percentage" in text:
        cursor.execute("SELECT AVG(score) FROM marks WHERE student_id= ?", (student_id,))
        avg= cursor.fetchone()[0]
        return f"Your calculated average is {avg: .2f}%" if avg else "No data available."

    # 2. Query: TOTAL
    elif "total" in text or "sum" in text or "aggregate" in text:
        cursor.execute("SELECT SUM(score) FROM marks WHERE student_id= ?", (student_id,))
        total = cursor.fetchone()[0]
        return f"Your total aggregate score is {total}."if total else "No data available."

    # 3. Query: HIGHEST
    elif "highest" in text or "max" in text or "best" in text or "top" in text:
        cursor.execute("SELECT subject, MAX(score) FROM marks WHERE student_id = ?",(student_id,))
        row= cursor.fetchone()
        return f"Your highest score is {row[1]} in {row[0]}." if row else "No data."
    # 4. Query: MINIMUM
    elif "lowest" in text or "min" in text or "worst" in text:
        cursor.execute("SELECT subject , MIN(score) FROM marks WHERE student_id = ?", (student_id,))
        row=cursor.fetchone()
        return f"Your lowest score is {row[1]} in {row[0]}." if row else "No data."
    # 5. Query: SPECIFIC SUBJECT (e.g. "Python","Math")
    cursor.execute("SELECT subject, score FROM marks WHERE student_id = ?",(student_id,))
    rows= cursor.fetchall()

    for subject, score in rows:
        #Check if the subject name (like "python") appears in the user's text
        if subject.lower() in text:
            #Determination of pass or fail (assuming 40 is the passing marks)
            status="PASS" if score >= 40 else "FAIL"
            return f"You scored {score} in {subject}.Status: {status}"
    # 6. Default: SHOW ALL MARKS
    if "marks" in text or "result" in text or "score" in text or "show" in text:
        #Calculate Summary stats
        total_score= sum(row[1] for row in rows)
        num_subjects=len(rows)
        percentage= total_score/ num_subjects if num_subjects > 0 else 0
        #Determination of overall Pass/Fail (Fail if any subject is <40)
        final_status = "PASS"
        for row in rows:
            if row[1]<40:
                final_status = "FAIL"
                break
        #Create the table
        table = tabulate(rows, headers=["Subject", "Score"], tablefmt= "grid")

        #Add the ReportCard Summary below the table
        summary = f"\nTotal: {total_score} | Percentage: {percentage:.2f}% | Overall Status: {final_status}"
        return "\n" + table + "\n" + summary
    return "I didn't understand. Try asking for 'Average', 'Total', or a Subject name."
if __name__=="__main__":
    main()





