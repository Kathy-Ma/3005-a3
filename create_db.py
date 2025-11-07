import psycopg2

db_name = "student_db_test"
db_password = ""

def createDb():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user='postgres',
            password=db_password,
            host='localhost',
            port= '5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # creating db
        cursor.execute("CREATE DATABASE %s", db_name)

        conn.close()
    except:
        print("Failed to create database. Possibly due to existing database with same name")

def connect():
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user="postgres",
            password=db_password,
            host="localhost",
            port="5432"
        )
        return conn
    except:
        print("Failed to connect")

def createTable():
    conn = connect()
    cursor = conn.cursor()

    try:
        # create the table
        cursor.execute("""
            CREATE TABLE students (
                student_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                enrollment_date DATE
                );
            """)
        conn.commit()
    except:
        print("Could not create table. Possibly because a table already exists with the same name")
    conn.close()

def addStudents():
    conn = connect()
    cursor = conn.cursor()
    try:
        # add students
        cursor.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');""")
        conn.commit()
    except:
        print("Could not add students. Possibly because a student with the given email already exists")
    conn.close()

def main():
    createDb()
    createTable()
    addStudents()

main()