from flask import Flask, render_template

app = Flask(__name__)

# Define the root route
@app.route('/')
def index():
    user = {'name': 'Blair'}
    return render_template('index.html', user=user)

# Define route for Genre
@app.route('/genre')
def genre():
    user = {'name': 'Blair'}
    return render_template('Genre.html', user=user)

# Define route for Contact
@app.route('/contact')
def contact():
    user = {'name': 'Blair'}
    return render_template('Contact.html', user=user)

# Define route for Login/Sign-in
@app.route('/login')
def login():
    user = {'name': 'Blair'}
    return render_template('Login_Sign-in.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
