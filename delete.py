from db_connection import get_connection

def show_student(mycursor, roll_number):
    """Fetches and displays the student record for the given roll number."""
    mycursor.execute("SELECT * FROM student WHERE roll_number = %s", (roll_number,))
    rows = mycursor.fetchall()

    if len(rows) == 0:
        print(f"\nNo student found with Roll Number {roll_number}.")
        return False
    else:
        print(f"\n{'='*65}")
        print(f"{'Roll No':<10} {'First Name':<15} {'Last Name':<15} {'CGPA':<8} {'Admission Date'}")
        print(f"{'='*65}")
        for row in rows:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<15} {row[3]:<8} {row[4]}")
        print(f"{'='*65}")
        return True

def main():
    try:
        conn = get_connection()
        mycursor = conn.cursor()

        print("--- Delete Student Record ---")
        roll_number = int(input("Enter Roll Number of the student to delete: "))

        # Show the record before deleting
        found = show_student(mycursor, roll_number)
        if not found:
            return

        # Confirm deletion
        confirm = input("\nAre you sure you want to delete this record? (yes/no): ").strip().lower()

        if confirm in ('yes', 'y'):
            mycursor.execute("DELETE FROM student WHERE roll_number = %s", (roll_number,))
            print(f"\nRecord deleted successfully! Rows affected: {mycursor.rowcount}")
        else:
            print("\nDeletion cancelled.")

    except ValueError as val_err:
        print(f"\nInput Error: Please enter a valid Roll Number ({val_err})")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        mycursor.close()
        conn.close()

if __name__ == "__main__":
    main()
