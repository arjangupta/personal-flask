from flask import Flask

app = Flask(__name__)

@app.route('/home')
def display_welcome_message():
    return "Welcome to Arjan Gupta's personal website"