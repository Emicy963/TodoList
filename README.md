# Todos Project

## Project Overview

This Fullstack project is a **todos application** developed using the Django framework and Django Rest Framework. The app allows users to create and manage todos. It also integrates third-party API data into the todos, making it a dynamic and feature-rich platform.

## 🚀 Features

- Create, edit, and delete todos.
- Third-party API integration for dynamic data.
  
## 📋 Technologies Used

- **Django**: Backend framework used for managing models, views, and templates.
- **Django Rest Framework**: Framework for creat API endpoints.
- **PostgreSQL**: Database used in production for reliable data storage.
- **Bootstrap**: For responsive and modern design.
- **HTML/CSS**: Template styling and structure.

## 🔧 Installation and Setup

### 📋 Pre-requisites
Before running this project, ensure you have the following installed:

- Python >= 3.9
- pip (Python package manager)
- PostgreSQL (for production database)


### 🛠️ Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/emicy963/todos-app.git
    cd todo-app
    ```

2. Set up a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Make sure PostgreSQL is running, and create a database for the project.
    - Update the `DATABASES` configuration in the `settings.py` file to connect to your PostgreSQL instance.

5. Run database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the blog in your browser:
    - Open `http://127.0.0.1:8000` in your web browser.

### 🔐 Environment Variables

Set the following environment variables in a `.env` file to securely configure your project:

```bash
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=your_domain_or_ip
DATABASE_URL=postgres://username:password@localhost:5432/your_db_name

```
## Usage

[Provide brief instructions on how to use the Todos App, e.g.:]

- Access the admin panel at `/admin` to manage todos
- Visit the homepage to view todos

## 🤝 Contributing

Welcome contributions to improve this todos apps! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and here to the project's coding standards.

### Reporting Issues

If you find a bug or have a suggestion for improvement, please open an issue on the GitHub repository. Provide as much detail as possible, including steps to reproduce the issue if applicable.

## 📝 Licença

This project is under the MIT license. View the archive `LICENSE` for more details.

## 👥 Author

Cafu Dev - [Emicy963](https://github.com/Emicy963)
Email: [Emicy963](emicy963@proton.me)
