from project import generate_response
import sqlite3
import pytest

#CITATION: Consulted AI (Gemini) for syntax on creating an in-memory (RAM)
#SQLite database using pytest fixtures. This ensures tests do not overwrites the actual 'results.db' file.
@pytest.fixture
def mock_conn():
    """
    Creates a temporary database in memory for testing purposes.
    """
    conn=sqlite3.connect(":memory:")
    c= conn.cursor()
    #Create a simple table structure for the test
    c.execute("CREATE TABLE marks (student_id INTEGER, subject TEXT, score INTEGER)")

    #Insert dummy data: Total= 180, Avg = 90, Max=95 (Math)
    c.execute("INSERT INTO marks VALUES (1, 'Math',95)")
    c.execute("INSERT INTO marks VALUES (1, 'English', 85)")
    return conn

def test_average_logic(mock_conn):
    """
    Test if the word 'average' correctly triggers the AVG calculation.
    """
    #logic: (95+85)/2=90
    response = generate_response(mock_conn,1,"What is my average?")
    assert "90.00%" in response

def test_total_logic(mock_conn):
    """
    Test if the word 'sum' correctly triggers the SUM calculation.
    """
    #logic: 95+85=180
    response= generate_response(mock_conn,1,"calculate sum")
    assert "180" in response

def test_subject_search(mock_conn):
    """
    Test if mentioning a subject name returns that specific score.
    """
    response = generate_response(mock_conn,1,"marks in Math")
    assert "95" in response
    assert "Math" in response

def test_unknown_query(mock_conn):
    """
    Test if a nonsense query returns the default help message.
    """
    response= generate_response(mock_conn,1,"hello world")
    assert "I didn't understand" in response


