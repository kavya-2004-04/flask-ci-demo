from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello():
    return "hello kavya welcome to ci/cd! "

if __name__ == '__main__':
    application.run(debug=False, host="0.0.0.0", port=5000)

