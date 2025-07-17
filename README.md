# 📚 EdTech Assignment Tracker

A simplified assignment tracking system for an EdTech platform that allows teachers to post assignments and students to submit them.

---
## Screenshot
<img width="1024" height="1024" alt="screenshot" src="https://github.com/user-attachments/assets/3e7cab4c-feb7-46ba-86ba-b64c624bea7d" />

## ✅ Features Implemented

### 🔒 Authentication (Role-Based)
- Signup & Login with role: `teacher` or `student`
- JWT-based authentication
- Role-based API access

### 📌 Assignment Management (Teacher)
- Create assignment (`POST /assignments/`)
- View all submissions for an assignment (`GET /assignments/{assignment_id}/submissions/`)

### ✍️ Submission Management (Student)
- Submit assignment content (`POST /assignments/{assignment_id}/submit/`)

---

## 🧱 System Architecture

- **Backend:** FastAPI (Python)
- **Database:** SQLite
- **Frontend:** HTML/CSS/JavaScript (Vanilla)
- **Auth:** JWT tokens (role: student / teacher)

---

## 🧩 Entities & Relationships

| Entity       | Fields |
|--------------|--------|
| **User**     | id, name, email, password, role |
| **Assignment** | id, title, description, due_date, teacher_id (FK) |
| **Submission** | id, content, student_id (FK), assignment_id (FK), timestamp |

### Relationships
- One **Teacher** → Many **Assignments**
- One **Student** → Many **Submissions**
- One **Assignment** → Many **Submissions**

---

## 🚀 API Endpoints

| Method | Endpoint | Role | Description |
|--------|----------|------|-------------|
| POST | `/signup` | All | Register a new user |
| POST | `/login` | All | Login and get JWT token |
| POST | `/assignments/` | Teacher | Create an assignment |
| POST | `/assignments/{assignment_id}/submit/` | Student | Submit an assignment |
| GET | `/assignments/{assignment_id}/submissions/` | Teacher | View all submissions |

---

## 🔐 Authentication Strategy

- JWT Token stored in `Authorization: Bearer <token>`
- Role-based access checks for each protected route
- Secure password hashing using `passlib`

---

## 🌐 Frontend UI

| Page | Description |
|------|-------------|
| `/teacher.html` | Form to create assignments |
| `/student.html` | Form to submit assignments |
| `/submissions.html` | View all submissions for a specific assignment |

---

## 🔧 How to Run

1. Install requirements:
   ```bash
   pip install -r requirements.txt


📦 Bonus Features
✅ File upload support for student submissions

✅ Swagger/OpenAPI documentation at /docs

✅ Clean UI with simple JavaScript frontend

✅ SQLite-based setup (portable)

📈 Future Scaling Ideas
Migrate DB to PostgreSQL

Add pagination, search filters

Add teacher dashboard with analytics

Use Redis for caching submissions

Deploy on cloud with Docker + CI/CD

## How to Access Swagger Docs:
Once your FastAPI app is running (using uvicorn main:app --reload), open the following URL in your browser:

bash
Copy
Edit
http://localhost:8000/docs

## Author 
Jitendra kumar
