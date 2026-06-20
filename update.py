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

        print("--- Update Student Record ---")
        roll_number = int(input("Enter Roll Number of the student to update: "))

        # Show current record
        found = show_student(mycursor, roll_number)
        if not found:
            return

        # Ask which field to update
        print("\nWhich field do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. CGPA")
        print("4. Admission Date")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            new_value = input("Enter new First Name: ")
            mycursor.execute("UPDATE student SET first_name = %s WHERE roll_number = %s", (new_value, roll_number))
        elif choice == '2':
            new_value = input("Enter new Last Name: ")
            mycursor.execute("UPDATE student SET last_name = %s WHERE roll_number = %s", (new_value, roll_number))
        elif choice == '3':
            new_value = float(input("Enter new CGPA: "))
            mycursor.execute("UPDATE student SET CGPA = %s WHERE roll_number = %s", (new_value, roll_number))
        elif choice == '4':
            new_value = input("Enter new Admission Date (YYYY-MM-DD): ")
            mycursor.execute("UPDATE student SET admission_date = %s WHERE roll_number = %s", (new_value, roll_number))
        else:
            print("\nInvalid choice!")
            return

        print(f"\nRecord updated successfully!")

        # Show updated record
        print("\nUpdated Record:")
        show_student(mycursor, roll_number)

    except ValueError as val_err:
        print(f"\nInput Error: Please enter data in the correct format ({val_err})")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        mycursor.close()
        conn.close()

if __name__ == "__main__":
    main()