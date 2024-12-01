from flask import Flask, render_template

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
    return render_template('Login_Sign-in.html')

if __name__ == '__main__':
    app.run(debug=True)
