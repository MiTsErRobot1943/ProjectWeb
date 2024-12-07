from flask import Flask, render_template, request, redirect, url_for, flash

#imports file from model.py for database
from model import db, bcrypt, User

app = Flask(__name__) # Don't remove or shit hits the fan - just reminder for me
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize database and bcrypt
db.init_app(app)
bcrypt.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()



# Setting up navigation
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/genre')
def genre():
    return render_template('Genre.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/Login_Sign-in')
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.')

    return render_template('Login_Sign-in.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('sign_up'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully!')
        return redirect(url_for('login'))

    return render_template('signup.html')
# Ended setup of navigation

#Runs the application
if __name__ == '__main__':
    app.run(debug=True)
