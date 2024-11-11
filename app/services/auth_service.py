import logging
from app.repositories import UserRepository
from app.utils.password_utils import hash_password, check_password
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthService:
    @staticmethod
    def register_user(email, password, first_name, last_name, phone_no, location, country):
        logging.info("Registering user: %s", email)
        
        # Validate input
        if not email or not password or not first_name or not last_name:
            logging.warning("Missing required fields for registration.")
            return None, 'Missing required fields'
        
        # Check if the email already exists
        if AuthService.email_exists(email):
            logging.warning("Email already exists: %s", email)
            return None, 'You already have an account with this email'
        
        password_hash = hash_password(password)
        user = UserRepository.create(email, password_hash, first_name, last_name, phone_no, location, country)
        logging.info("User registered successfully: %s", user.id)
        return user, None  # Return user and no error message

    @staticmethod
    def generate_username(first_name):
        base_username = first_name.lower()
        username = base_username
        count = 1

        # Check for uniqueness
        while UserRepository.get_by_username(username):
            username = f"{base_username}{count}"
            count += 1

        return username

    @staticmethod
    def login_user(email, password):
        logging.info("Login attempt for email: %s", email)
        
        # Validate input
        if not email or not password:
            logging.warning("Missing required fields for login.")
            return None, None, 'Missing required fields'
        
        user = UserRepository.get_by_email(email)
        
        if not user:
            logging.warning("User not found: %s", email)
            return None, None, 'User not found'
        
        if check_password(user.password_hash, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            logging.info("User logged in successfully: %s", email)
            return access_token, refresh_token, None
        
        logging.warning("Invalid credentials for email: %s", email)
        return None, None, 'Invalid credentials'

    @staticmethod
    def logout_user(jti):
        logging.info("Logging out user with JWT ID: %s", jti)
        return jti  # Return the JWT ID for blacklisting

    @staticmethod
    def get_user_profile(user_id):
        logging.info("Fetching user profile for user ID: %s", user_id)
        user = UserRepository.get_by_id(user_id)
        if not user:
            logging.warning("User not found for ID: %s", user_id)
        return user

    @staticmethod
    def user_exists(username):
        return UserRepository.get_by_username(username) is not None

    @staticmethod
    def email_exists(email):
        exists = UserRepository.get_by_email(email) is not None
        logging.info("Email exists check for %s: %s", email, exists)
        return exists
