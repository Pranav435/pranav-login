import os
from flask import Flask, render_template, request
from helpers import email
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app=Flask(__name__)
db=scoped_session(sessionmaker(create_engine(os.getenv("DATABASE_URL"))))

@app.route("/",methods=["GET","POST"])
def index():
	if request.method=="GET":
		return render_template("index.html")
	else:
		name=request.form.get("name")
		email=request.form.get("email")
		password=request.form.get("password")
		if len(password) < 8:
			return render_template("result.html",message="Error. The password is too small.")
		db.execute("insert into users ( name, email, password ) values ( :name, :email, :password )",{"name":name,"email":email,"password":password})
		#email(os.getenv("EMAIL"),os.getenv("PASSWORD"),email_id,"Success","Successfully stored your data")
		return render_template("result.html",message="Successfully logged in")

@app.route("/registrants")
def registrants():
	return render_template("registrants.html",names=names)