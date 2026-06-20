from db_connection import get_connection
import queries

def main():
    # Step 1: Connect to the database
    try:
        conn = get_connection()
        mycursor = conn.cursor()
    except Exception:
        print("Failed to initialize database connection.")
        return

    # Step 2: Create the table if it doesn't exist
    mycursor.execute(queries.CREATE_TABLE_QUERY)

    # Step 3: Get user input
    print("--- Enter Student Details ---")
    try:
        roll_number = int(input("Roll Number: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        cgpa = float(input("CGPA: "))
        admission_date = input("Admission Date (YYYY-MM-DD): ")

        # Step 4: Prepare data record as a tuple
        record = (roll_number, first_name, last_name, cgpa, admission_date)

        # Step 5: Execute the insert query with the record data
        mycursor.execute(queries.INSERT_STUDENT_QUERY, record)

        print(f"\nStudent {first_name} {last_name} inserted successfully!")
    except ValueError as val_err:
        print(f"\nInput Error: Please enter data in the correct format ({val_err})")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        mycursor.close()
        conn.close()

if __name__ == "__main__":
    main()