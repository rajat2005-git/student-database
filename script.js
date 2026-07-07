const API_URL = 'http://127.0.0.1:5000/students';

// Tab Navigation Logic
function showTab(tabId) {
    document.querySelectorAll('.nav-tabs button').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    
    event.target.classList.add('active');
    document.getElementById(tabId).classList.add('active');

    // Fetch data fresh from the database when viewing
    if(tabId === 'view') {
        loadStudentData();
    }
}

// Fetch and display data from Flask API
function loadStudentData() {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('studentTableBody');
            tableBody.innerHTML = ''; 
            
            data.forEach(student => {
                const row = `<tr>
                    <td>${student.roll_number}</td>
                    <td>${student.first_name}</td>
                    <td>${student.last_name}</td>
                    <td>${student.CGPA}</td>
                    <td>${student.admission_date}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(err => console.error("Error loading data:", err));
}

// Add Student (POST)
document.getElementById('addForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const data = {
        roll_number: document.getElementById('roll').value,
        first_name: document.getElementById('fname').value,
        last_name: document.getElementById('lname').value,
        cgpa: document.getElementById('cgpa').value,
        admission_date: document.getElementById('date').value
    };

    fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        document.getElementById('addForm').reset();
    });
});

// Update Student (PUT)
document.getElementById('updateForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const roll_number = document.getElementById('updateRoll').value;
    const data = {
        field: document.getElementById('updateField').value,
        new_value: document.getElementById('newValue').value
    };

    fetch(`${API_URL}/${roll_number}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        document.getElementById('updateForm').reset();
    });
});

// Delete Student (DELETE)
document.getElementById('deleteForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const roll_number = document.getElementById('deleteRoll').value;

    fetch(`${API_URL}/${roll_number}`, {
        method: 'DELETE'
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        document.getElementById('deleteForm').reset();
    });
});

// Load default data on page load
window.onload = () => {
    loadStudentData();
};