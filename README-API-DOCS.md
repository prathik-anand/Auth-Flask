# Authentication API Documentation

## Overview

The Authentication API provides a robust and secure way to manage user authentication and authorization in web applications. It allows users to register, log in, log out, refresh their access tokens, and retrieve their profile information. This API is essential for any application that requires user accounts and secure access to resources.

## Usefulness of the API

1. **User Management**: The API facilitates user registration and login, enabling applications to manage user accounts effectively. This is crucial for applications that require personalized experiences, such as social media platforms, e-commerce sites, and content management systems.

2. **Security**: By implementing token-based authentication, the API enhances security. Access tokens are short-lived, reducing the risk of unauthorized access, while refresh tokens allow users to maintain their sessions without re-entering credentials frequently.

3. **Seamless User Experience**: The ability to refresh tokens without requiring users to log in again improves the overall user experience. Users can stay logged in for extended periods while maintaining security.

4. **Profile Management**: The API allows users to retrieve their profile information, enabling applications to display personalized content and settings based on user data.

## Interlinking of Endpoints

The endpoints in the Authentication API are interlinked to provide a cohesive user experience:

- **Registration**: Users start by registering their accounts through the `/register` endpoint. Upon successful registration, they can log in to obtain access and refresh tokens.

- **Login**: The `/login` endpoint authenticates users and issues tokens. The access token is used for subsequent requests to protected resources, while the refresh token is stored securely for future use.

- **Token Refresh**: When the access token expires, the `/refresh` endpoint allows users to obtain a new access token using their refresh token, ensuring uninterrupted access to the application.

- **Logout**: The `/logout` endpoint invalidates the current session by blacklisting the access token, enhancing security when users choose to log out.

- **Profile Retrieval**: The `/profile` endpoint allows users to access their account details, which can be displayed in the user interface, providing a personalized experience.

## Integration for UI Developers

For UI developers looking to integrate this Authentication API into their applications, the following steps outline a typical workflow:

1. **User Registration**:
   - Create a registration form in the UI that collects the username, email, and password.
   - On form submission, send a `POST` request to the `/register` endpoint with the user data in JSON format.
   - Handle the response to inform the user of successful registration or any errors.

   **Curl Example:**
   ```bash
   curl -X POST http://localhost:5010/auth/register \
   -H "Content-Type: application/json" \
   -d '{"email": "newuser@example.com", "password": "securepassword", "first_name": "John", "last_name": "Doe", "phone_no": "1234567890", "location": "New York", "country": "USA"}'
   ```

2. **User Login**:
   - Implement a login form that collects the user's email and password.
   - On submission, send a `POST` request to the `/login` endpoint.
   - Store the received access token and refresh token securely (e.g., in local storage or cookies) for future API calls.

   **Curl Example:**
   ```bash
   curl -X POST http://localhost:5010/auth/login \
   -H "Content-Type: application/json" \
   -d '{"email": "newuser@example.com", "password": "securepassword"}'
   ```

3. **Access Protected Resources**:
   - For any API calls that require authentication, include the access token in the `Authorization` header.
   - Example: `Authorization: Bearer your_access_token`.

4. **Token Refresh**:
   - Monitor the expiration of the access token. If it expires, use the refresh token to obtain a new access token by sending a `POST` request to the `/refresh` endpoint.

   **Curl Example:**
   ```bash
   curl -X POST http://localhost:5010/auth/refresh \
   -H "Content-Type: application/json" \
   -d '{"refresh_token": "your_refresh_token"}'
   ```

5. **User Logout**:
   - Provide a logout option in the UI. When the user chooses to log out, send a `POST` request to the `/logout` endpoint with the access token in the header.

   **Curl Example:**
   ```bash
   curl -X POST http://localhost:5010/auth/logout \
   -H "Content-Type: application/json" \
   -d '{"refresh_token": "your_refresh_token"}'
   ```

6. **Display User Profile**:
   - After successful login, retrieve the user profile by sending a `GET` request to the `/profile` endpoint with the access token.

   **Curl Example:**
   ```bash
   curl -X GET http://localhost:5010/auth/profile \
   -H "Authorization: Bearer your_access_token"
   ```

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

## Notes
- Ensure that your API handles these responses appropriately, returning the correct HTTP status codes.
- Adjust the JSON payload in the request body as needed for your specific use case.
- Replace `localhost:5000` with your actual server address and port if different.


