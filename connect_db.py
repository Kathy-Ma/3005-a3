import psycopg2

db_name = "student_db"
db_password = ""

def connect():
    try:
        db = psycopg2.connect(
            dbname=db_name,
            user="postgres",
            password=db_password,
            host="localhost",
            port="5432"
        )
        return db
    except:
        print("Failed to connect")
    

def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    for row in cur.fetchall():
        print(row)
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date): 
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
        print("Student added")
    except:
        print("Student failed to add")

    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        conn.commit()
        print("Student email updated")
    except:
        print("Failed to update email")
    conn.close()

def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        print("Student deleted!")
    except:
        print("Failed to delete student")
    conn.close()

def main():

    if __name__ == "__main__":
        getAllStudents()
        addStudent("hana", "reed", "hana.reed@example.com", "2023-09-05")
        # updateStudentEmail(1, "john.newemail@example.com")
        deleteStudent(1)
        getAllStudents()


main()