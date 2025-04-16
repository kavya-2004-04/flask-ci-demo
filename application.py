from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello():
    return "Hello, CI/CD!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

