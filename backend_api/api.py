from flask import Flask

app = Flask(__name__)

@app.route('/home')
def display_welcome_message():
    return "<p> Welcome to Arjan Gupta's personal website! </p> <p> This website is currently under construction. Please check back later. Thank you! <p>"