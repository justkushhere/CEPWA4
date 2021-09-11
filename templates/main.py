import flask
import json, os
from flask import render_template, request, session

app = flask. Flask (__name__)
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800

app.config.update(SECRET_KEY=os.urandom(24))

app.config.from_object(__name__)


@app.route("/")
def root():
  return render_template("securesites.html")

@app.route('/login', methods = ['GET' , 'POST'])
def login():
  logindata = {}
  if os.path.exists("user.json"):
    with open("user.json") as userfile:
      logindata = json.load(userfile)
  if request.form.get("Login"):
    if logindata[request.form.get("emailID")] == request.form.get("masterkeyID"):
      app.secret_key = request.form.get("emailID")
      session['emailID']=request.form.get("emailID")
      return render_template("password-display.html")
    else:
      return render_template("Sign-In.html")
  else:
    logindata[request.form.get("emailID")] = request.form.get("masterkeyID")
    with open("user.json", "w") as userfile:
      json.dump(logindata, userfile)
    return render_template("login.html")


@app.route('/signup', methods = ['GET' , 'POST'])
def signup():
  logindata = {}
  if os.path.exists("user.json"):
    with open("user.json") as userfile:
      logindata = json.load(userfile)
  if request.form.get("masterkeyID") == request.form.get("confirmmasterkeyID"):
      if request.form.get("Login"):
        if logindata[request.form.get("emailID")] == request.form.get("masterkeyID"):
          app.secret_key = request.form.get("emailID")
          session['emailID']=request.form.get("emailID")
          return render_template("password-display.html")
        else:
          return render_template("Sign-In.html")
      else:
        logindata[request.form.get("emailID")] = request.form
        with open("user.json", "w") as userfile:
          json.dump(logindata, userfile)
        return render_template("pasword-display.html")
   else:
       return render_template("Sign-Up.html")
