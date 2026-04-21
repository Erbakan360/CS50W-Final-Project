# CS50W Final Project: TODO Web Application

## Introduction
The TODO web application is a user-friendly tool designed to help individuals efficiently manage their tasks. By registering or logging in to their accounts, users can easily create, edit, duplicate, delete, and mark tasks as complete. The application is mobile-responsive and utilizes Django, HTML, CSS, and Python.

## Distinctiveness and Complexity
The TODO web application satisfies the distinctiveness and complexity requirements by providing a unique combination of features that build upon the practices of the standard projects in CS50W. This project is not a social network, nor an e-commerce site, and it has been developed with a focus on usability and user experience.

The application includes multiple models, such as the Task and User models, to handle the storage and retrieval of data. The models are defined in the `models.py` file and establish relationships between tasks and users. This allows each task to be associated with a specific user, ensuring privacy and data integrity.

The back-end logic for each view, including registration, login, and task management, is implemented in the `views.py` file. It handles user authentication, task creation and modification, and other operations required for task management.

The URL patterns for the application are defined in the `urls.py` file, which maps each URL to the corresponding view function. This enables proper routing and navigation within the application.

The front-end of the application is implemented using HTML templates located in the `templates/TODO` directory. The `layout.html` template provides a base structure for common elements, such as the side bar, which are shared across multiple pages. The `register.html` and `login.html` templates display the user registration and login forms, respectively. The `index.html` template is responsible for displaying the main page, where active tasks are shown and can be sorted by priority, deadline, or date added. The `completed_tasks.html` template displays completed tasks, allowing users to edit, duplicate, delete, or mark them as incomplete. The `create.html` template presents a form for creating new tasks.

The `static/TODO` directory contains static files, including the `styles.css` file, which defines the global styles for the application. These styles ensure a consistent and visually appealing user interface.

To run the TODO web application, follow these steps:

1. Run the Django migrations with the command `python manage.py makemigrations TODO`.
2. Apply the migrations with the command `python manage.py migrate`.
3. Start the development server with the command `python manage.py runserver`.
4. Access the application in your web browser at `http://127.0.0.1:8000/`.

In conclusion, the TODO web application is a unique task management tool that combines usability, functionality, and user experience. Its distinct features, such as user registration, task creation and modification, sorting capabilities, and strict permissions, set it apart from other projects in the course. The use of Django, Python, CSS and HTML ensures a robust and responsive application. By following the provided instructions, you can easily set up and run the TODO web application to enhance your task management and productivity.
