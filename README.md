# 💼 JobTrackr - AI-Powered Job Application Tracker

A modern Job Application Management System built with **Django** that allows users to manage and track their job applications from a centralized dashboard.

The system provides job application management, application status tracking, search and filtering, interview management, and an AI-powered job description analysis feature using the **Google Gemini API**.

---

## Features

- User Registration
- User Login & Logout
- Custom User Authentication
- Dashboard
- Job Application Management
- Application Status Tracking
- Application Search
- Application Filtering
- Application Sorting
<!-- - Pagination -->
- Application Details
- Interview Management
- Upcoming Interviews
- Interview Details
- Interview Notes
- Meeting Link
- AI-Powered Job Description Analysis
- Required Skills Analysis
- Technology Analysis
- Experience Analysis
- Interview Preparation Suggestions
- Responsive UI
- Toast Notifications
- Delete Confirmation Modal

---

## Technology Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- HTML5
- CSS3
- JavaScript
- Google Gemini API

---

## Project Structure

```text
AI-Powered-Job-Application-Tracker/
│
├── accounts/
├── applications/
├── config/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── media/
│
├── manage.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/MaksudaParvin/AI-Powered-Job-Application-Tracker.git
```

### Go to project directory

```bash
cd AI-Powered-Job-Application-Tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=your-db-name
DB_USER=postgres
DB_PASSWORD=your-postgresql-password
DB_HOST=localhost
DB_PORT=5432

GEMINI_API_KEY=your-gemini-api-key
```

### Run Migration

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

---

## Database

Database: PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE your-db-name;
```

Configure the PostgreSQL database credentials in the `.env` file.

Example:

```text
Database Name: jobtracker
Database User: postgres
Database Host: localhost
Database Port: 5432
```

Run migrations after configuring the database:

```bash
python manage.py migrate
```

---

## AI Configuration

The project uses the **Google Gemini API** for AI-powered job description analysis.

Add your Gemini API key to the `.env` file:

```env
GEMINI_API_KEY=your-gemini-api-key
```

## Demo Video

<p align="center">

<a href="YOUR_DEMO_VIDEO_URL">
  ▶ Watch AI Powered Job Application Tracker Demo Video
</a>

</p>

<p align="center">
<b>Demo Video: JobTrackr - AI-Powered Job Application Tracker</b>
</p>

---

## Functionalities

- ✔ User Registration
- ✔ User Login
- ✔ User Logout
- ✔ Custom User Authentication
- ✔ Dashboard
- ✔ Add Job Application
- ✔ View Job Application
- ✔ Edit Job Application
- ✔ Delete Job Application
- ✔ Application Search
- ✔ Application Filtering
- ✔ Application Sorting
<!-- - ✔ Pagination -->
- ✔ Application Status Tracking
- ✔ Interview Management
- ✔ Add Interview
- ✔ View Interview
- ✔ Edit Interview
- ✔ Delete Interview
- ✔ Upcoming Interviews
- ✔ Interview Details
- ✔ Interview Notes
- ✔ Meeting Link
- ✔ AI Job Description Analysis
- ✔ Required Skills Analysis
- ✔ Technology Analysis
- ✔ Experience Analysis
- ✔ Interview Preparation
- ✔ REST API Integration
- ✔ PostgreSQL Database
- ✔ Responsive Design
- ✔ Toast Notifications
- ✔ Delete Confirmation Modal

---



## Author

**Maksuda Parvin**

Department of Computer Science & Engineering

Bangladesh University of Business and Technology (BUBT)

---

## License

This project is developed for learning and academic purposes.