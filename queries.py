# SQL Query templates

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS student (
    roll_number INT, 
    first_name VARCHAR(20), 
    last_name VARCHAR(20), 
    CGPA DECIMAL(4,2), 
    admission_date DATE
)
"""

INSERT_STUDENT_QUERY = """
INSERT INTO student (roll_number, first_name, last_name, CGPA, admission_date) 
VALUES (%s, %s, %s, %s, %s)
"""