import flask
import json, os
from flask import render_template, request, session, Flask, flash, jsonify
from flask import Markup

app = flask. Flask (__name__)
SESSION_TYPE = "filesystem"
PERMANENT_SESSION_LIFETIME = 1800

app.config.update(SECRET_KEY=os.urandom(24))

app.config.from_object(__name__)

def writetojson(dict,nameID,emailID,masterkeyID):
    dictionary = {
    "name":nameID,
    "Email":emailID,
    "Password":masterkeyID
    }
    with open("sample.json","w") as outfile:
        json.dump(dictionary,outfile)

    return dictionary









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
    print("ohno")
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
    return render_template("Sign-In.html")

@app.route('/signup', methods = ['GET' , 'POST'])
def signup():
  logindata = {}
  if os.path.exists("user.json"):
    with open("user.json") as userfile:
      logindata = json.load(userfile)
  if (request.form.get("masterkeyID") == request.form.get("confirmmasterkeyID")) and (request.form.get("masterkeyID") != None):
      if request.form.get("submit"):
          logindata = writetojson(logindata,request.form.get("nameID"),request.form.get("emailID"),request.form.get("masterkeyID"))
          #logindata[request.form.get("emailID")] = request.form
      #with open("user.json", "w") as userfile:
          #json.dump(logindata, userfile)
      with open('sample.json', 'r') as myfile:
          data = myfile.read()
          print(data)
      return render_template('password-display.html', jsonfile=json.dumps(data))
  elif request.form.get("masterkeyID") == None:
      #return render_template("modal_template.html")
      return render_template("Sign-Up.html")
  else:
    return render_template('Sign-Up.html')

@app.route('/password_display', methods = ['GET','POST'])
def password_display():
    print("1")
    # read file
    with open('sample.json', 'r') as myfile:
        data = myfile.read()
        print(data)
    return render_template('password-display.html', jsonfile=json.dumps(data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
