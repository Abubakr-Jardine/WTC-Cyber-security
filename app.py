from flask import Flask, request,url_for, redirect, render_template

app = Flask(__name__)

@app.route("/",methods = ["POST","GET"])
def index():
    if request.method == "POST":
        if request.form.get("action1") == "Login":
            return redirect(url_for("login_page"))
    return render_template("index.html")

@app.route("/login")
def login_page():
    return "This is the login page"