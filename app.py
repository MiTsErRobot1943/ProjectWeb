from flask import Flask, render_template

app = Flask(__name__)

# Define a proper route using URL notation
@app.route('/')
def hello_world(name=None):
    user = {'name': 'Blair'}
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
