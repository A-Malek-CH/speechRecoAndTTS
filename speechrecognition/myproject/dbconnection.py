import random
import mysql.connector
import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MALEK.admin123",
    database="myproject"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS myproject")
cursor.execute("""CREATE TABLE IF NOT EXISTS 
 jokes (
    id INT PRIMARY KEY,
    joke TEXT NOT NULL,
    author VARCHAR(100)
);
""")

"""for testing"""
"""cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)"""

"""to insert just once"""
cursor.execute("SELECT COUNT(*) FROM jokes")
result = cursor.fetchone()

if result[0] == 0 :
    cursor.execute("""
    INSERT INTO  jokes (id, joke, author) VALUES
    (1, 'Why don''t scientists trust atoms? Because they make up everything!', 'Unknown'),
    (2, 'Why was the math book sad? Because it had too many problems.', 'Unknown'),
    (3, 'Why did the scarecrow win an award? Because he was outstanding in his field!', 'Unknown');
    """)

""" current joke selector  """
def selectRandomJoke():
    cursor.execute("SELECT * FROM jokes")
    res = cursor.fetchall()
    return random.choice(res)[1]

"""table show """

cursor.execute("SELECT * FROM jokes")
rows = cursor.fetchall()

"""for row in rows:
    print(f"ID: {row[0]}, Joke: {row[1]}, Author: {row[2]}")"""

"""lessons:"""
cursor.execute("""CREATE TABLE IF NOT EXISTS lessons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    day_of_week VARCHAR(10) NOT NULL,  # Use VARCHAR for day names
    period INT NOT NULL,  # Use INT for period number
    lesson VARCHAR(20) NOT NULL,  # Allow for lesson names up to 20 characters
    CONSTRAINT unique_lesson UNIQUE (day_of_week, period)  # Ensure unique combinations
);
""")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM jokes")
result2 = cursor.fetchone()

if result2[0] == 0 :
    cursor.execute("""
    INSERT INTO lessons (day_of_week, period, lesson) VALUES
        ('Monday', 1, 'Lesson A'),
        ('Monday', 2, 'Lesson B'),
        ('Monday', 3, 'Lesson C'),
        ('Monday', 4, 'Lesson D'),
        ('Sunday', 1, 'Lesson A'),
        ('Sunday', 2, 'Lesson B'),
        ('Sunday', 3, 'Lesson C'),
        ('Sunday', 4, 'Lesson D'),
        ('Tuesday', 1, 'Lesson A'),
        ('Tuesday', 2, 'Lesson B'),
        ('Tuesday', 3, 'Lesson C'),
        ('Tuesday', 4, 'Lesson D'),
        ('Wednesday', 1, 'Lesson A'),
        ('Wednesday', 2, 'Lesson B'),
        ('Wednesday', 3, 'Lesson C'),
        ('Wednesday', 4, 'Lesson D'),
        ('Thurdsay', 1, 'Lesson A'),
        ('Thurdsay', 2, 'Lesson B'),
        ('Thurdsay', 3, 'Lesson C'),
        ('Thurdsay', 4, 'Lesson D'),
    """)


def get_next_lesson():
    """Retrieves the next lesson based on the current day and time."""

    # Get current day and time
    today = datetime.datetime.today().strftime("%A")  # Get day of the week as full name
    now = datetime.datetime.now().time()  # Get current time

    # Compare time to period start times
    if now < datetime.time(8, 30):
        day = "Monday"
        period = 1
    elif now < datetime.time(10, 0):
        day = today
        period = 1
    elif now < datetime.time(13, 0):
        day = today
        period = 2
    elif now < datetime.time(14, 30):
        day = today
        period = 3
    else:
        day = today
        period = 4

    # Retrieve lesson for the specific day and period
    cursor.execute("SELECT lesson FROM lessons WHERE day_of_week = %s AND period = %s", (day, period))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return "No lessons found for this time."

"""# test
next_lesson = get_next_lesson()
if next_lesson:
    print(f"The next lesson is: {next_lesson}")
else:
    print("No lessons found for this time.")
"""
