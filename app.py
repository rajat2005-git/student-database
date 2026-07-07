from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connection import get_connection
import queries

# 1. Update Flask initialization to serve static files from the current folder
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Initialize database table on startup
try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_QUERY)
    conn.close()
except Exception as e:
    print(f"Database initialization error: {e}")

# 2. Add this route to serve your index.html at the root URL!
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        
        for row in rows:
            if row.get('admission_date'):
                row['admission_date'] = str(row['admission_date'])
                
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        record = (data['roll_number'], data['first_name'], data['last_name'], data['cgpa'], data['admission_date'])
        cursor.execute(queries.INSERT_STUDENT_QUERY, record)
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@app.route('/students/<int:roll_number>', methods=['PUT'])
def update_student(roll_number):
    data = request.json
    field = data['field']
    new_value = data['new_value']
    
    valid_fields = ['first_name', 'last_name', 'CGPA', 'admission_date']
    if field not in valid_fields:
        return jsonify({"error": "Invalid field"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = f"UPDATE student SET {field} = %s WHERE roll_number = %s"
        cursor.execute(query, (new_value, roll_number))
        
        if cursor.rowcount == 0:
            return jsonify({"message": "No student found with that Roll Number"}), 404
            
        return jsonify({"message": "Student updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

@app.route('/students/<int:roll_number>', methods=['DELETE'])
def delete_student(roll_number):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE roll_number = %s", (roll_number,))
        
        if cursor.rowcount == 0:
            return jsonify({"message": "No student found with that Roll Number"}), 404
            
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)