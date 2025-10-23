#novos exercícios de sql com python usando um novo db com vários dados
import sqlite3
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
def execute_query(conn, query):
    """ Execute a single query """
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def main():
    database = "school.db"
    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        age integer,
                                        grade text
                                    ); """
    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        credits integer
                                    ); """
    sql_create_enrollments_table = """ CREATE TABLE IF NOT EXISTS enrollments (
                                        student_id integer NOT NULL,
                                        course_id integer NOT NULL,
                                        FOREIGN KEY (student_id) REFERENCES students (id),
                                        FOREIGN KEY (course_id) REFERENCES courses (id)
                                    ); """
    conn = create_connection(database)
    if conn is not None:
        execute_query(conn, sql_create_students_table)
        execute_query(conn, sql_create_courses_table)
        execute_query(conn, sql_create_enrollments_table)
    else:
        print("Error! cannot create the database connection.")
# if __name__ == '__main__':
#     main()
    
#fim do código

#adicionando novos dados

def add_student(conn, student):
    sql = ''' INSERT INTO students(name,age,grade)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid
def add_course(conn, course):
    sql = ''' INSERT INTO courses(name,credits)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, course)
    conn.commit()
    return cur.lastrowid
def add_enrollment(conn, enrollment):
    sql = ''' INSERT INTO enrollments(student_id,course_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, enrollment)
    conn.commit()
    return cur.lastrowid
def main():
    database = "school.db"
    conn = create_connection(database)
    if conn is not None:
        student_1 = ('Alice', 20, 'A')
        student_2 = ('Bob', 22, 'B')
        course_1 = ('Mathematics', 4)
        course_2 = ('History', 3)
        student_1_id = add_student(conn, student_1)
        student_2_id = add_student(conn, student_2)
        course_1_id = add_course(conn, course_1)
        course_2_id = add_course(conn, course_2)
        enrollment_1 = (student_1_id, course_1_id)
        enrollment_2 = (student_2_id, course_2_id)
        add_enrollment(conn, enrollment_1)
        add_enrollment(conn, enrollment_2)
    else:
        print("Error! cannot create the database connection.")
# if __name__ == '__main__':
#     main()
    
#acessando os dados
def fetch_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
def fetch_courses(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    for row in rows:
        print(row)
def fetch_enrollments(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM enrollments")
    rows = cur.fetchall()
    for row in rows:
        print(row)
def main():
    database = "school.db"
    conn = create_connection(database)
    if conn is not None:
        print("Students:")
        fetch_students(conn)
        print("\nCourses:")
        fetch_courses(conn)
        print("\nEnrollments:")
        fetch_enrollments(conn)
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    main()