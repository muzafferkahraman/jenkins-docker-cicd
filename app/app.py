from flask import Flask

app = Flask(__name__)

@app.route('/')
def message():
    return 'Wilkommen zum my repos'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
