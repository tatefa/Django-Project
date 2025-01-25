# Django Chat Application

A real-time chat application built using Django and WebSockets. This project allows users to sign up, log in, and engage in one-to-one private messaging with other registered users.

---

## Features

- **User Authentication**:
  - Sign up and log in functionality.
  - Secure user sessions.
  
- **Chat Functionality**:
  - Real-time messaging using WebSockets.
  - Old messages retrieved and displayed in the chat interface.

- **User Interface**:
  - Collapsible menu showing all registered users.
  - Responsive and user-friendly chat interface.

---

## Technologies Used

- **Backend**: Django, Django Channels
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Real-Time Communication**: WebSockets
- **Hosting (optional)**: PythonAnywhere

---

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system.
- A virtual environment (recommended).
- Git installed for version control.

###Set up a virtual environment:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

###Install Dependencies Required

####Project structure
django-chat-app/
├── chat/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── consumers.py
│   ├── models.py
│   ├── views.py
├── my_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .gitignore

