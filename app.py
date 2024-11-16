from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session management

# Simulate a database with a list to store users
users = []

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Simulate storing user data securely (e.g., hashed password)
        hashed_password = generate_password_hash(password, method='sha256')
        users.append({'username': username, 'email': email, 'password': hashed_password})

        flash('Signup successful!')
        return redirect(url_for('signup'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
