# Exam Token Sales Platform

A full-stack web application for selling and validating **one-time exam access tokens**. Built with **React** for the frontend and **Django / Django REST Framework** for the backend. This platform demonstrates secure token management, payment integration, and modular architecture for full-stack applications.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Environment Variables](#environment-variables)
6. [Running the Application](#running-the-application)
7. [Project Structure](#project-structure)
8. [Future Improvements](#future-improvements)
9. [License](#license)

---

## Project Overview
This platform allows users to purchase **exam tokens** and gain controlled access to services (e.g., WhatsApp groups). Each token is **one-time use** and securely managed via backend APIs. The project highlights full-stack development, secure API design, and modular project structure.

---

## Features
- React frontend with responsive UI for token purchase and access
- Django backend with REST API endpoints
- Secure one-time token generation and usage tracking
- Payment integration (Paystack)
- Modular project structure for easy maintenance and scalability
- Git version control with separate folders for frontend and backend

---

## Tech Stack
- **Frontend:** React, Tailwind CSS
- **Backend:** Django, Django REST Framework, PostgreSQL
- **Payment Integration:** Paystack
- **Version Control:** Git / GitHub
- **Deployment (optional):** Railway, Vercel, or similar

---

## Installation

### Clone the repository
```bash
git clone https://github.com/kosirufus/Juike-Exams-Token-Sale-full-stack-web-app.git
cd Juike-Exams-Token-Sale-full-stack-web-app
Backend Setup
bash
Copy code
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Frontend Setup
bash
Copy code
cd frontend
npm install
npm start
Environment Variables
Create a .env file in the backend folder with the following:

ini
Copy code
SECRET_KEY=your-django-secret-key
DEBUG=True
PAYSTACK_SECRET_KEY=your-paystack-secret-key
DATABASE_URL=your-database-url
Ensure .env is added to .gitignore to avoid exposing secrets.

Running the Application
Start the backend server:

bash
Copy code
cd backend
python manage.py runserver
Start the frontend server:

bash
Copy code
cd frontend
npm start
Open your browser at http://localhost:3000 to interact with the frontend. Backend APIs are available at http://localhost:8000.

Project Structure
csharp
Copy code
exam-token-sales-fullstack/
├── backend/           # Django project
│   ├── manage.py
│   ├── your apps/
│   └── requirements.txt
├── frontend/          # React project
│   ├── package.json
│   ├── src/
│   └── public/
├── .gitignore
└── README.md
Future Improvements
Deploy full-stack app to production (Railway / Vercel / Docker)

Add user authentication and admin panel

Enhance token analytics and reporting

Integrate additional payment providers

License
MIT License © 2025 Kosisochukwu Rufus Ezeagu
