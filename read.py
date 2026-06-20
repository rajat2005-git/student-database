from db_connection import get_connection

def main():
    try:
        conn = get_connection()
        mycursor = conn.cursor()

        # Execute SELECT query to read all records
        mycursor.execute("SELECT * FROM student")
        rows = mycursor.fetchall()

        # Display the records
        if len(rows) == 0:
            print("\nNo student records found in the database.")
        else:
            print(f"\n{'='*65}")
            print(f"{'Roll No':<10} {'First Name':<15} {'Last Name':<15} {'CGPA':<8} {'Admission Date'}")
            print(f"{'='*65}")
            for row in rows:
                print(f"{row[0]:<10} {row[1]:<15} {row[2]:<15} {row[3]:<8} {row[4]}")
            print(f"{'='*65}")
            print(f"Total Records: {len(rows)}")

    except Exception as e:
        print(f"\nAn error occurred while reading data: {e}")
    finally:
        mycursor.close()
        conn.close()

if __name__ == "__main__":
    main()
