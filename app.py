from flask import Flask, request,flash,url_for

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return "Welcome"