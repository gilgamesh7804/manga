from flask import Flask, request, jsonify, render_template, redirect, url_for
import json

app = Flask(__name__)

# Dummy user data for demonstration
users = [
    {'username': 'shin', 'email': 'shin@gmail.com', 'password': '123'},
    {'username': 'kyoko', 'email': 'kyo@gmail.com', 'password': '321'}
]

# Route for welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for manga page
@app.route('/manga')
def manga():
    return render_template('manga.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for sign in page
@app.route('/signin')
def signin():
    return render_template('signin.html')

# Route for registration
@app.route('/register', methods=['POST', 'GET'])
def register():
    message = request.args.get('message')
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if the user already exists
        for user in users:
            if user['email'] == email:
                return redirect(url_for('register', message="User already exists"))

        # Add the new user to the list
        new_user = {'username': username, 'email': email, 'password': password}
        users.append(new_user)
        return redirect(url_for('signin', message="You have successfully registered. You can now sign in."))

    else:
        return render_template('register.html', message=message)

# Route for login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Check if the user exists and the password matches
        for user in users:
            if user['email'] == email and user['password'] == password:
                return jsonify({'message': 'Login successful'}), 200

        return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
