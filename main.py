from flask import Flask

app = Flask(__name__)

@app.route('/')
def respond():
    return "Hi Brendan"
