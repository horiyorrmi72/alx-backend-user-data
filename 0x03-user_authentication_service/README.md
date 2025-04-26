# User Authentication

This directory contains a Python-based user authentication service. It provides functionalities for user registration, login, session management, password reset, and profile access. The service is built using Flask for the backend and SQLite for the database (using sqlalchemy engine).

## Features

- **User Registration**: Allows users to register with an email and password.
- **Login**: Validates user credentials and creates a session.
- **Session Management**: Supports session creation, retrieval, and destruction.
- **Profile Access**: Provides access to user profiles when logged in.
- **Password Reset**: Generates reset tokens and updates passwords securely.

## Directory Structure

```
.
├── app.py                  # Flask application for the authentication service
├── auth.py                 # Authentication logic and helper methods
├── db.py                   # Database interaction and ORM setup
├── main.py                 # End-to-end test script for the service
├── user.py                 # User model definition
├── env/                    # Virtual environment directory
└── a.db                    # SQLite database file (auto-generated)
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd /0x03-user_authentication_service
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application
Start the server:
```bash
python app.py
```
The server will run on `http://localhost:5000`.

### 5. Run the Test Script
Execute the end-to-end test script:
```bash
python main.py
```

## API Endpoints

### 1. **Register a User**
- **Endpoint**: `/users`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  - Success: `{"email": "user@example.com", "message": "user created"}`
  - Failure: `{"message": "email already registered"}`

### 2. **Login**
- **Endpoint**: `/sessions`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  - Success: `{"email": "user@example.com", "message": "logged in"}`
  - Failure: HTTP 401 Unauthorized

### 3. **Logout**
- **Endpoint**: `/sessions`
- **Method**: `DELETE`
- **Cookies**: `session_id`
- **Response**:
  - Success: Redirects to `/`
  - Failure: HTTP 403 Forbidden

### 4. **Access Profile**
- **Endpoint**: `/profile`
- **Method**: `GET`
- **Cookies**: `session_id`
- **Response**:
  - Success: `{"email": "user@example.com"}`
  - Failure: HTTP 403 Forbidden

### 5. **Request Password Reset Token**
- **Endpoint**: `/reset_password`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "email": "user@example.com"
  }
  ```
- **Response**:
  - Success: `{"email": "user@example.com", "reset_token": "<token>"}`
  - Failure: HTTP 403 Forbidden

### 6. **Update Password**
- **Endpoint**: `/reset_password`
- **Method**: `PUT`
- **Payload**:
  ```json
  {
    "email": "user@example.com",
    "reset_token": "<token>",
    "new_password": "newpassword123"
  }
  ```
- **Response**:
  - Success: `{"email": "user@example.com", "message": "Password updated"}`
  - Failure: HTTP 403 Forbidden

## Testing

The main.py script provides an end-to-end test for the service. It performs the following operations:
1. Registers a user.
2. Attempts to log in with an incorrect password.
3. Tries to access the profile without being logged in.
4. Logs in with correct credentials.
5. Accesses the profile while logged in.
6. Logs out.
7. Requests a password reset token.
8. Updates the password using the reset token.
9. Logs in with the new password.

Run the script:
```bash
python main.py
```

## Dependencies

- Python 3.6+
- Flask
- SQLAlchemy
- bcrypt

## License
