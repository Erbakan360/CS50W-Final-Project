# CS50W-Final-Project

A custom-designed web application that serves as the capstone for the CS50W course.

A robust, mobile-responsive task management tool designed to streamline personal productivity. Unlike standard course projects, this application focuses on a highly interactive user experience for managing life workflows through a clean, custom interface.

Key Features:
    Task Lifecycle Management: Full CRUD (Create, Read, Update, Delete) functionality allowing users to create, edit, duplicate, and delete tasks.
    Smart Sorting: An organized dashboard where active tasks can be dynamically sorted by priority, deadline, or the date they were added.
    Task States: Dedicated views for active and completed tasks, with the ability to toggle tasks between states or "duplicate" existing ones for recurring needs.
    Personalized Security: A custom user authentication system ensuring that every task is private and associated strictly with the individual's account.
    Responsive UI: A sidebar-driven layout designed with custom CSS to ensure the app is fully functional and visually consistent on both desktop and mobile devices.

Tech Stack:
    Backend: Python, Django (utilizing multiple models with relational data integrity).
    Frontend: HTML5 (Template inheritance via layout.html), CSS3 (Global styling via styles.css).
    Database: SQL (SQLite) handling User and Task relationships.

Requirements: https://cs50.harvard.edu/web/projects/final/capstone/

# How to run

python manage.py makemigrations TODO

python manage.py migrate

python manage.py runserver
