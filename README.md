# Todo App Made Using Django

## Description  
A web-based **Todo Application** built with **Django Framework** that allows users to manage their personal tasks efficiently.  
It includes secure **user authentication (login & registration)**, ensuring that each user can **only view and manage their own tasks**.  
The app uses **Django Widget Tweaks** for form customization and **Bootstrap** for a clean and responsive UI.

---

## Features

- User **registration and login system** using Django’s built-in authentication.
- Each user can **Add, Update, Delete, and Mark tasks as Complete**.
- Tasks are **user-specific**, ensuring privacy and data separation.
- **Django Widget Tweaks** used for customizing form design.
- **Bootstrap** integrated for a modern, responsive UI.
- Follows Django’s **MVC (Model-View-Template)** architecture.

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)
- **Libraries Used:**  
  - `django-widget-tweaks`
  - `django.contrib.auth`

---

## How It Works

1. Users can **register** for a new account or **log in** if they already have one.  
2. Once logged in, each user can:
   - **Add new tasks** with titles and descriptions.  
   - **Mark tasks as complete** when finished.  
   - **Edit or delete** tasks they own.  
3. The app ensures **authorization** — users cannot modify others’ tasks.  
4. **Widget Tweaks** enhances form styling for a better user experience.

---

## Run It Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django-todo-app.git
   cd django-todo-app

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate      # On macOS/Linux
    venv\Scripts\activate         # On Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Start the development server:
    ```bash
    python manage.py runserver

