from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data for demonstration
users = [
    {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'},
    {'username': 'user2', 'email': 'user2@example.com', 'password': 'password2'}
]

# Register endpoint to register new users
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    for user in users:
        if user['email'] == email:
            return jsonify({'message': 'User already exists'}), 400

    # Add the new user to the list
    new_user = {'username': username, 'email': email, 'password': password}
    users.append(new_user)
    return jsonify({'message': 'User registered successfully'}), 200

# Login endpoint to authenticate users
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if the user exists and the password matches
    for user in users:
        if user['email'] == email and user['password'] == password:
            return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
