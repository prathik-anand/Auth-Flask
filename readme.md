# Authentication API

## Overview

The Authentication API is a secure and robust solution for managing user authentication and authorization in web applications. It provides essential features such as user registration, login, logout, token refresh, and profile management, making it suitable for applications that require user accounts and secure access to resources.

## Features

- **User Management**: Facilitates user registration and login, allowing applications to manage user accounts effectively.
- **Security**: Implements token-based authentication with short-lived access tokens and refresh tokens for enhanced security.
- **Seamless User Experience**: Allows users to refresh tokens without re-entering credentials, improving user experience.
- **Profile Management**: Enables users to retrieve and manage their profile information, including email and other attributes.

## API Endpoints

### Base URL
`http://localhost:5010/auth`

### Endpoints

#### 1. User Registration

- **Endpoint**: `/register`
- **Method**: `POST`
- **Description**: Registers a new user.

**Request:**
```json
{
    "email": "newuser@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe",
    "phone_no": "1234567890",
    "location": "New York",
    "country": "USA"
}
```

**Success Response:**
```json
{
    "message": "User registered successfully",
    "user_id": 1
}
```

**Failure Responses:**
- `400 Bad Request`: Missing required fields.
- `409 Conflict`: Email already exists.

#### 2. User Login

- **Endpoint**: `/login`
- **Method**: `POST`
- **Description**: Logs in a user.

**Request:**
```json
{
    "email": "newuser@example.com",
    "password": "securepassword"
}
```

**Success Response:**
```json
{
    "access_token": "your_access_token",
    "refresh_token": "your_refresh_token"
}
```

**Failure Responses:**
- `401 Unauthorized`: Missing required fields or invalid credentials.

#### 3. Refresh Token

- **Endpoint**: `/refresh`
- **Method**: `POST`
- **Description**: Refreshes the access token using the refresh token.

**Request:**
```json
{
    "refresh_token": "your_refresh_token"
}
```

**Success Response:**
```json
{
    "access_token": "new_access_token"
}
```

**Failure Response:**
- `401 Unauthorized`: Invalid refresh token.

#### 4. Logout

- **Endpoint**: `/logout`
- **Method**: `POST`
- **Description**: Logs out a user by invalidating the refresh token.

**Request:**
```json
{
    "refresh_token": "your_refresh_token"
}
```

**Success Response:**
```json
{
    "message": "User logged out successfully"
}
```

**Failure Response:**
- `401 Unauthorized`: Invalid refresh token.

#### 5. Get User Profile

- **Endpoint**: `/profile`
- **Method**: `GET`
- **Description**: Retrieves the user's profile information.

**Request:**
- **Header**: `Authorization: Bearer your_access_token`

**Success Response:**
```json
{
   "email": "newuser@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone_no": "1234567890",
    "location": "New York",
    "country": "USA"
}
```

**Failure Response:**
- `401 Unauthorized`: Invalid access token.

## Integration for UI Developers

### Typical Workflow

1. **User Registration**: Create a registration form and send a `POST` request to `/register`.
2. **User Login**: Implement a login form and send a `POST` request to `/login`. Store the received tokens securely.
3. **Access Protected Resources**: Include the access token in the `Authorization` header for API calls.
4. **Token Refresh**: Monitor the access token expiration and use the refresh token to obtain a new access token.
5. **User Logout**: Provide a logout option that sends a `POST` request to `/logout`.
6. **Display User Profile**: Retrieve the user profile by sending a `GET` request to `/profile`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prathik-anand/Auth-Flask.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Auth-Flask
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY="your_secret_key"
JWT_SECRET_KEY="your_jwt_secret_key"
DATABASE_URL="your_database_url"
CORS_ALLOWED_ORIGINS="http://localhost:3000" #Client URL
```

## DATABASE TABLE
Please run below sql to create table in RDBMS
```
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_no VARCHAR(15),
    location VARCHAR(100),
    country VARCHAR(50)
);
```

## Running the Application

To run the application, execute:
```bash
python run.py
```

## Contact

Your Name - [prathik.a@outlook.in](mailto:prathik.a@outlook.in)

Project Link: [https://github.com/prathik-anand/Auth-Flask.git