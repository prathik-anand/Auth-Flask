import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token, create_refresh_token
from app.services.auth_service import AuthService
from app import blacklist  # Import the blacklist

bp = Blueprint('auth', __name__, url_prefix='/auth')  # Prefix for authentication endpoints

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    logging.info("Registering user with email: %s", data.get('email'))

    # Extract data directly from the request
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_no = data.get('phone_no')
    location = data.get('location')
    country = data.get('country')

    # Call the service layer to handle registration
    user, error_message = AuthService.register_user(email, password, first_name, last_name, phone_no, location, country)

    if error_message:
        logging.warning("Registration failed: %s", error_message)
        return jsonify({'message': error_message}), 409  # Conflict

    logging.info("User registered successfully: %s", user.id)
    return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    logging.info("User login attempt for email: %s", email)

    access_token, refresh_token, error_message = AuthService.login_user(email, password)
    if error_message:
        logging.warning("Login failed: %s", error_message)
        return jsonify({'message': error_message}), 401  # Unauthorized

    logging.info("User logged in successfully: %s", email)
    return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # Require a valid refresh token
def refresh():
    current_user_id = get_jwt_identity()
    logging.info("Refreshing access token for user ID: %s", current_user_id)

    new_access_token = create_access_token(identity=current_user_id)
    return jsonify({'access_token': new_access_token}), 200

@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    logging.info("Logging out user with JWT ID: %s", jti)

    AuthService.logout_user(jti)
    blacklist.add(jti)
    logging.info("User logged out successfully.")
    return jsonify({'message': 'Logout successful'}), 200

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    logging.info("Fetching profile for user ID: %s", current_user_id)

    user = AuthService.get_user_profile(current_user_id)
    if not user:
        logging.warning("User not found: %s", current_user_id)
        return jsonify({'message': 'User not found'}), 404  # Not Found

    return jsonify({
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_no': user.phone_no,
        'location': user.location,
        'country': user.country
    }), 200
