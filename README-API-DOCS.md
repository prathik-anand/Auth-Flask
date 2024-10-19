# Authentication API Documentation

## Overview

The Authentication API provides a robust and secure way to manage user authentication and authorization in web applications. It allows users to register, log in, log out, refresh their access tokens, and retrieve their profile information. This API is essential for any application that requires user accounts and secure access to resources.

## Usefulness of the API

1. **User Management**: The API facilitates user istration and login, enabling applications to manage user accounts effectively. This is crucial for applications that require personalized experiences, such as social media platforms, e-commerce sites, and content management systems.

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

2. **User Login**:
   - Implement a login form that collects the user's email and password.
   - On submission, send a `POST` request to the `/login` endpoint.
   - Store the received access token and refresh token securely (e.g., in local storage or cookies) for future API calls.

3. **Access Protected Resources**:
   - For any API calls that require authentication, include the access token in the `Authorization` header.
   - Example: `Authorization: Bearer your_access_token`.

4. **Token Refresh**:
   - Monitor the expiration of the access token. If it expires, use the refresh token to obtain a new access token by sending a `POST` request to the `/refresh` endpoint.
   - Update the stored access token with the new one received in the response.

5. **User Logout**:
   - Provide a logout option in the UI. When the user chooses to log out, send a `POST` request to the `/logout` endpoint with the access token in the header.
   - Clear the stored tokens from the client-side storage.

6. **Display User Profile**:
   - After successful login, retrieve the user profile by sending a `GET` request to the `/profile` endpoint with the access token.
   - Use the returned user data to personalize the UI, such as displaying the username and email.

## API Endpoints

## Base URL
`http://localhost:5000/auth`


## Endpoints

### 1. User Registration


- **Endpoint**: `/register`
- **Method**: `POST`
- **Description**: Registers a new user.

```
curl -X POST http://localhost:5000/auth/register \
-H "Content-Type: application/json" \
-d '{"email": "testuser@example.com", "password": "yourpassword", "first_name": "John", "last_name": "Doe", "phone_no": "1234567890", "location": "New York", "country": "USA"}'
```

#### Request
- **Content-Type**: `application/json`
- **Body**:
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

#### Success Response
- **Status Code**: `201 Created`
- **Body**:
```json
{
    "message": "User registered successfully",
    "user_id": 1
}
```

#### Failure Responses
- **Status Code**: `400 Bad Request`
    - **Body**:
    ```json
    {
        "message": "Missing required fields"
    }
    ```
- **Status Code**: `409 Conflict`   
    - **Body**:
    ```json
    {
        "message": "User Name already exists"
    }
    ```
- **Status Code**: `409 Conflict`   
    - **Body**:
    ```json
    {
        "message": "Email already exists"
    }
    ``` 

### 2. User Login

- **Endpoint**: `/login`
- **Method**: `POST`
- **Description**: Logs in a user.

```
curl -X POST http://localhost:5000/api/auth/login \
-H "Content-Type: application/json" \
-d '{"email": "testuser@example.com", "password": "yourpassword"}'
``` 

#### Request
- **Content-Type**: `application/json`
- **Body**:
```json
{
    "email": "newuser@example.com",
    "password": "securepassword"
}
``` 
--- 
#### Success Response
- **Status Code**: `200 OK`
- **Body**:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjYzMjYyOCwianRpIjoiZjYyYzMxZjItZjYyZC00YzYyLTgwNjItNjYyYjYyYjYyYjYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzIyNjMyNjI4LCJleHAiOjE3MjI2MzMyMjh9.62c31f2-f62d-4c62-8062-662b662b662b",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjYzMjYyOCwianRpIjoiZjYyYzMxZjItZjYyZC00YzYyLTgwNjItNjYyYjYyYjYyYjYyIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTcyMjYzMjYyOCwiZXhwIjoxNzIyNjMzMjI4fQ.62c31f2-f62d-4c62-8062-662b662b662b"
}
```

#### Failure Responses
- **Status Code**: `401 Unauthorized`
    - **Body**:
    ```json
    {
        "message": "Missing Required Fields"
    }
    ```
- **Status Code**: `401 Unauthorized`
    - **Body**:
    ```json
    {
        "message": "Invalid Credentials"
    }
    ``` 
    
### 3. Refresh Token    

- **Endpoint**: `/refresh`
- **Method**: `POST`
- **Description**: Refreshes the access token using the refresh token.

```
curl -X POST http://localhost:5000/api/auth/refresh \
-H "Content-Type: application/json" \
-d '{"refresh_token": "yourrefreshToken"}'
``` 

#### Request
- **Header**:
    - `Authorization`: `Bearer <refresh_token>`

#### Success Response
- **Status Code**: `200 OK`
- **Body**:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjYzMjYyOCwianRpIjoiZjYyYzMxZjItZjYyZC00YzYyLTgwNjItNjYyYjYyYjYyYjYyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzIyNjMyNjI4LCJleHAiOjE3MjI2MzMyMjh9.62c31f2-f62d-4c62-8062-662b662b662b"
}
``` 

#### Failure Responses
- **Status Code**: `401 Unauthorized`
    - **Body**:
    ```json
    {
        "message": "Invalid Refresh Token"
    }
    ```

### 4. Logout

- **Endpoint**: `/logout`
- **Method**: `POST`
- **Description**: Logs out a user by invalidating the refresh token.

```
curl -X POST http://localhost:5000/api/auth/logout \
-H "Content-Type: application/json" \
-d '{"refresh_token": "yourrefreshToken"}'
``` 

#### Request
- **Header**:
    - `Authorization`: `Bearer <refresh_token>` 

#### Success Response
- **Status Code**: `200 OK`
- **Body**:
```json
{
    "message": "User logged out successfully"
}
```

#### Failure Responses
- **Status Code**: `401 Unauthorized`
    - **Body**:
    ```json
    {
        "message": "Invalid Refresh Token"
    }
    ```

### 5. Get User Profile

- **Endpoint**: `/profile`
- **Method**: `GET`
- **Description**: Retrieves the user's profile information.

```
curl -X GET http://localhost:5000/api/auth/profile \
-H "Authorization: Bearer youraccesstoken"
```

#### Request
- **Header**:
    - `Authorization`: `Bearer <access_token>`  

#### Success Response
- **Status Code**: `200 OK`
- **Body**:
```json
{
    "username": "newuser",
    "email": "newuser@example.com"
}

#### Failure Responses
- **Status Code**: `401 Unauthorized`
    - **Body**:
    ```json
    {
        "message": "Invalid Access Token"
    }
    ``` 
    
---

## Notes
- Ensure that your API handles these responses appropriately, returning the correct HTTP status codes.
- Adjust the JSON payload in the request body as needed for your specific use case.
- Replace `localhost:5000` with your actual server address and port if different.


