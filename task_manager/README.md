# Task Management API Documentation

This document provides an overview of the Task Management API, including endpoints, data models, and real-time data streaming.

## API Endpoints

### Authentication Endpoints

#### Register User

- **URL**: `/api/register/`
- **Method**: POST
- **Description**: Allows users to register by providing a username and password.

#### Login User

- **URL**: `/api/login/`
- **Method**: POST
- **Description**: Allows users to log in by providing a username and password. Returns JWT tokens for authentication.

### Task Management Endpoints

#### List and Create Tasks

- **URL**: `/api/tasks/`
- **Method**: GET (List), POST (Create)
- **Description**: Lists all tasks belonging to the authenticated user. Allows users to create new tasks.

#### Retrieve, Update, and Delete Task

- **URL**: `/api/tasks/<task_id>/`
- **Method**: GET (Retrieve), PUT (Update), DELETE (Delete)
- **Description**: Retrieves, updates, or deletes a specific task identified by its ID.

## Data Models

### User Model

- **Fields**:
  - `username`: CharField (max length: 150)
  - `email`: EmailField (optional)
  - `password`: PasswordField

### Task Model

- **Fields**:
  - `user`: ForeignKey (to User model)
  - `title`: CharField (max length: 255)
  - `description`: TextField
  - `done`: BooleanField (default: False)
  - `created_at`: DateTimeField (auto-generated)
  - `updated_at`: DateTimeField (auto-generated)

## Real-Time Data Streaming

To stream real-time data updates, we utilize Django Channels, a library that extends Django to handle WebSockets, HTTP2, and other asynchronous protocols.

### Implementation Steps

1. **Install Channels**: Install Django Channels using `pip`.
2. **Configure Routing**: Define routing configuration in `task_manager/routing.py`.
3. **Create Consumers**: Implement consumers to handle WebSocket connections and data streaming.
4. **Configure ASGI**: Configure ASGI application in `task_manager/asgi.py`.
5. **Connect Frontend**: Connect the frontend to the WebSocket server to receive real-time updates.

## Additional Notes

- Ensure proper error handling and validation for all endpoints.
- Implement proper authentication and authorization mechanisms to secure the endpoints.
- Document any additional configuration or setup steps required for deployment.
- Provide clear and concise documentation comments within the codebase to aid developers in understanding the implementation details.

By following these guidelines, future developers can easily understand and work with the codebase to maintain and extend the task management system.