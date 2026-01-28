# 🎬 Cinema Management System

A **full-stack cinema ticket management system** built with a **Python backend** and a **web-based frontend**, designed to manage users, staff, and administrators while generating **batch-wise PDF tickets** automatically.

---

## 📌 Project Overview

This project provides a simple yet functional **cinema booking and management platform**.
It includes:

* Backend APIs for ticket and user management
* Frontend interfaces for **admin, staff, and customers**
* Automated **PDF ticket generation in batches**
* Database setup and migration scripts

The system is suitable for **college projects**, **mini projects**, or **cinema workflow demonstrations**.

---

## ✨ Key Features

* 🎟️ Cinema ticket generation system
* 📄 **Batch-wise PDF ticket creation**
* 👨‍💼 Admin panel for management
* 👨‍🔧 Staff interface for operations
* 🌐 User-friendly frontend UI
* ⚙️ Python backend with environment configuration
* 🗂️ Organized project structure (frontend + backend)

---

## 🛠️ Tech Stack

### Backend

* **Python**
* PDF generation library
* Environment-based configuration (`.env`)
* SQL for database migration

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript (Vanilla JS)**

---

## 📂 Project Structure

```text
cinema project by mango/
│
├── backend/
│   ├── main.py                  # Backend server logic
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables
│   ├── generated_pdfs/          # Auto-generated ticket PDFs
│   └── __pycache__/
│
├── frontend/
│   ├── index.html               # User interface
│   ├── admin.html               # Admin dashboard
│   ├── staff.html               # Staff panel
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── config.js
│
├── create_users.py              # Script to create default users
├── check_setup.py               # Setup validation script
├── migration_items_active.sql   # Database migration
└── start_backend.bat            # Backend startup script
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

### 2️⃣ Configure Environment Variables

Edit:

```text
backend/.env
```

Add database and application configuration as required.

---

### 3️⃣ Run Database Migration

```sql
migration_items_active.sql
```

---

### 4️⃣ Start the Backend

```bash
python backend/main.py
```

OR
Double-click:

```text
start_backend.bat
```

---

### 5️⃣ Run the Frontend

Open in browser:

```text
frontend/index.html
```

Admin and staff panels:

```text
frontend/admin.html
frontend/staff.html
```

---

## 📄 PDF Ticket Generation

* Tickets are generated **automatically in batches**
* Stored inside:

```text
backend/generated_pdfs/
```

* Each PDF represents a specific ticket batch range

---

## 🎯 Use Cases

* Cinema ticket management demo
* College / BCA / MCA project
* PDF automation systems
* Backend + frontend integration practice
* Batch processing applications

---

## ⚠️ Notes

* Designed for **educational and demo purposes**
* Not production-hardened
* Ensure correct Python and database configuration
* Frontend communicates with backend via JS config

---

## 📜 License

This project is open-source and intended for **learning and academic use**.
