import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2005',
            database='student_info',
            autocommit=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        raise