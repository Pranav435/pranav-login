import os
from flask import Flask, render_template, request
from helpers import email
names=[]
emails=[]
passwords=[]

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
	if request.method=="GET":
		return render_template("index.html")
	else:
		name=request.form.get("name")
		email_id=request.form.get("email")
		password=request.form.get("password")
		if len(password) < 8:
			return render_template("result.html",message="Error. The password is too small.")
		names.append(name)
		emails.append(email)
		passwords.append(password)
		#email(os.getenv("EMAIL"),os.getenv("PASSWORD"),email_id,"Success","Successfully stored your data")
		return render_template("result.html",message="Successfully logged in")

@app.route("/registrants")
def registrants():
	return render_template("registrants.html",names=names)