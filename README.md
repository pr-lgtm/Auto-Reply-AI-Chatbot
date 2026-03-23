# AUTO-REPLY AI CHATBOT FOR STUDENT RESULT QUERIES

#### Video Demo: https://youtu.be/yj326LIl3o4?si=9D2bov68jI_69mXU

#### Description

The **Auto-Reply AI Chatbot for Student Result Queries** is a Command Line Application written in Python that is intended to be an Intelligent Automated Support System that assists students with their result queries at an Academic Institution. This was my final project submission for CS50's Introduction to Computer Science course.

The *main objective* of this project was to provide a solution for students that would allow them to have more of a direct interaction with the results from the database as opposed to navigating through the various web interfaces or waiting on faculty responses on these results. This software allows students to simply 'ask' for their results in a conversational manner (e.g., "Did I pass?" or "What do I get for Statistics?") and provides an instant response based on data from the database. It combines the logical processing of Python with the relational nature of SQLite to provide the user with a seamless experience.

**Project Structure and Files**

This project has multiple files with various roles within its architecture. Listed below are the different file types that comprise this project as well as their rationale.

**1. Project.py**

*Project.py* is the central controller for the application, containing both its main logic loop and its various function definitions that accommodate the chat bot's operations.
The function **main()** serves as the entry point for the application. At this point, the application connects to the database, establishes a chat loop that continues receiving user-invoked input until such time as the user exits from within the application.

**User Login & Authentication:**

The function **login(conn)** handles user authentication by prompting the user for their unique student Roll Number, comparing it to what is stored in the database, and if valid, returning the Student ID as well as their Student Name, so that any queries made after that will be associated with the same Student.

**Chatbot Responses Generation:**

The function **generate_response(conn, student_id, text)** serves as the "brain" of the chatbot, where rather than using heavy Regular Expression matching techniques, it instead uses a simple keyword identification approach (by using the `in` keyword) to find the user's intent keywords like average, total or a Subject name. Once the user is identified, a secure SQL query is executed by utilizing the **sqlite3** library. If the user has asked for "Show all marks", a Summary of Statistics (Total, Percentage) will be computed and then the output will be formatted into a Professional looking Table using the **tabulate** library.

**2. results.db**

The SQLite Database file provides back-end storage for all of the application’s data.
*Rationale:* I chose SQLite as my Database engine because it is lightweight and serverless, which makes it ideal for use with a stand-alone application.
*Structure of the Database:* This application has a 2-table relational database consisting of **“students”** (holding student personal information such as Name and Roll Number) and **“marks”** (directly connecting back to the students table through foreign key(s) and storing subject marks). By breaking down our data as described here, we are abiding by Normalization principles that you learned about during CS50 SQL week and have reduced redundant data.

**3. test_project.py**

The **test_project.py** file is where all Unit Tests for testing a function's accuracy in FS- Dev solutions are documented according to best practices from the CS50 Unit Testing Course Week . The Unit Test framework we are using is **pytest** to otain correct results when calling the function named **generate_response** based on users intents (your intetation of the meaning on messages e.g. "average", "total"or by specific subject) and return the correct calculated output based on those intents.  Also we created test cases to verify that function we created to handle special cases of special characters (e.g. nonsense inputs like "hello world") and text that may contain all capital letters/functions or parts of it so that when we check these kinds of user inputs we get the correct "call for help" response from our application and not a crash of the application because of invalid input from the user.

**4. requirements.txt**

A conventional text document which defines the dependencies necessary for the correct operation of this project. Although most of this project is based on the Python standard library, this document registers all external libraries that could potentially be used later.

**5. create_db.py**

A setup script that initializes the databases with dummy student data for testing.

**Development techniques and design considerations**

**AI Logic (Rules-Based System)**

Today’s Artificial Intelligence is primarily performed using Large Language Models (LLM) to establish conclusions or decision-making. However, I would like to take a Computer Science approach to developing the AI for my project; I preferred to use a rule-based approach instead of relying on box-based libraries.

The rules engine in my chatbot operates using Python Code and conditional statements (if this, then that). Each time the end user provides input into the chatbot, it first retrieves any keywords found in the answer. For example, if the end user asks the question “How do I score in Maths,” the chatbot will identify the keyword “Maths” and run a SQL query based on that user’s Math information. By using a keyword, I was able to create an efficient, structured, and totally predictable process in the chatbot while eliminating all of the unpredictability that comes with using generative AI models.

**Access to the database**

Initially, I planned on storing the exam data in a CSV file (as we had done in earlier weeks of CS50). However, as the number of exam results continues to increase, a flat file will be less practical for managing that data due to the high number of reads per day; therefore, I chose to use SQL. Additionally, SQL provides the opportunity to calculate aggregate functions (such as AVG or SUM) through the use of the database engine, which will increase performance for those types of operations as opposed to needing to run those calculations inPython on a flat file first.

**User Experience (CLI)**

In my opinion, I felt that using a **Command Line Interface(CLI)** was more straightforward and effective than using a *GUI*. The user was able to concentrate on their conversation with me without any distractions caused by GUI elements. All the information presented in the CLI is formatted using f-strings to ensure that the information appears in an easily readable format for humans, as opposed to appearing as raw database records.

**How to Run?**

**1. Initialize the Database:** Ensure *results.db* is in the root directory.If not, you can generate it by running the provided setup script(if applicable) or importing the schema.

**2. Install Dependencies:** Run *pip install -r requirements.txt*(if  pytest or other non-standard libraries are used)

**3. Execute the Chatbot:** Run the command: **python project.py**

**4. Testing:** To verify the integrity of the code, run: **pytest test_project.py**

**Upcoming Enhancements**

Although the current iteration of this application is fully operational, I intend to enhance it in the future with a **Graphical User Interface (GUI)** developed with a GUI toolkit such as **tkinter** or deploy it as a web application with the **Flask framework**. A more complex **Natural Language Processing (NLP)** library could enable even more natural conversations.

This project was both an exciting and rewarding capstone experience for me during the course of CS50. I learned how to bring together the concepts of many different topics, such as logical reasoning, data structures and database design, into one holistic application.
