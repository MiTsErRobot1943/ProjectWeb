from flask import Flask, render_template

app = Flask(__name__)


@app.route('../templates/index.html')
def hello_world():  # put application's code here
    user = {'name': 'Blair'}
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
