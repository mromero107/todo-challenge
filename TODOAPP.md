# Invera Challenge: To-do App

This is a simple Django application for managing todo tasks.

## Endpoints

Swagger: `http://localhost:8000/api/docs`

- Tasks:
    - `GET /api/tasks/`
    - `POST /api/tasks/`

- Task:
    - `GET /api/tasks/{id}/`
    - `PUT /api/tasks/{id}/`
    - `PATCH /api/tasks/{id}/`
    - `DELETE /api/tasks/{id}/`


## Docker

To run the To-do App in Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t invera.todoapp:latest .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 invera.todoapp:latest
    ```

3. Open your web browser and visit `http://localhost:8000` to access the application.

4. Visit `http://localhost:8000/api/docs` to access the documentation of the API.

## Makefile: A fast path to deploy the App.
    To start the services:

    ```bash
    make start
    ```
    To stop the services:

    ```bash
    make stop
    ```

## Create superuser

    ```bash
    make create_superuser
    ```

## App Usage

- Create a new task by clicking on the "Add" button.
- Edit a task by clicking on the "Edit" button.
- Mark a task as done by checking the checkbox next to the task.
- Delete a task by clicking on the "Delete" button.
