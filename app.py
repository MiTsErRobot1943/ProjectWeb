from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    user = {'name': 'Blair'}
    return render_template('index.html', user=user)

# Define route for Genre
@app.route('/Genre.html')
def genre():
    user = {'name': 'Blair'}
    return render_template('Genre.html', user=user)

# Define route for Contact
@app.route('/Contact.html')
def contact():
    user = {'name': 'Blair'}
    return render_template('Contact.html', user=user)

# Define route for Login/Sign-in
@app.route('/Login_Sign-in.html')
def login():
    user = {'name': 'Blair'}
    return render_template('Login_Sign-in.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
