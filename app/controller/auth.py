from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, create_access_token, create_refresh_token
from app.services.auth_service import AuthService
from app import blacklist  # Import the blacklist

bp = Blueprint('auth', __name__, url_prefix='/auth')  # Prefix for authentication endpoints

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

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
        return jsonify({'message': error_message}), 409  # Conflict

    return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')  # Change to email
    password = data.get('password')

    access_token, refresh_token, error_message = AuthService.login_user(email, password)
    if error_message:
        return jsonify({'message': error_message}), 401  # Unauthorized

    return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # Require a valid refresh token
def refresh():
    # Get the current user's identity from the refresh token
    current_user_id = get_jwt_identity()
    # Create a new access token
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify({'access_token': new_access_token}), 200

@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Get the JWT ID from the current token
    jti = get_jwt()['jti']
    # Call the service to handle logout
    AuthService.logout_user(jti)
    # Add the token to the blacklist
    blacklist.add(jti)
    return jsonify({'message': 'Logout successful'}), 200

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = AuthService.get_user_profile(current_user_id)
    return jsonify({
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_no': user.phone_no,
        'location': user.location,
        'country': user.country
    }), 200
