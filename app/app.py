from flask import Flask

app = Flask(__name__)

@app.route('/')
def message():
    return 'Welcome to my repo'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
