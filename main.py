from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("securesites.html")
