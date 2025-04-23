#!/usr/bin/python3
"""
this module contains sample api to authetify users and admins
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpass"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    if verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Bad username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return jsonify({"message": "Admin Access: Granted"})
    return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)
