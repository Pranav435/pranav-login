import smtplib,ssl,csv
from email.message import EmailMessage

def email(email_id,password,to,subject,msg):
	"""
Sends an email with the given strings.
Inputs:
email_id: the email id that is used to log in to gmail as well as to send the mail from.
password: the password of the corresponding email id.
to: the mail id to send the email to.
subject: The subject of the email.
msg: The message body section of the email id.
returns:
No return value. The mail is sent, however.
Note: I've tried to comment this function as much so that you as well as any other reader of this function can understand how smtplib and the email.message modules work in python.
	"""
#	try:
	context=ssl.create_default_context()
	server=smtplib.SMTP("smtp.gmail.com",587) #This line basically sets up the server for use. We're currently using gmail's server, which is the recommended option. We are using 587, which is tls. I am planning to change that to 465, ssl, which is more secure, but for the time being, this is what i've set up for testing.
	server.starttls() #starts up the tls server for us.
	server.login(email_id,password) #uses the parameters email_id and password to login to gmail's server.
	message=EmailMessage() #creats an EmailMessage object, which basically helps us store info about our email that we're trying to send.
#now lets set some parameters.
	message.set_content(msg) #sets the body of the mail
	message["From"]=email_id #sets up the from attribute for the message object.
	message["Subject"]=subject #sets up the subject for our email id.
	message["To"]=to #you know what this does, specifies who the mail should send to.
#lets now send the mail.
	server.send_message(message)
#finally, lets close the server.
	server.quit()
#	except:
#		return -1

def csv_write(filename,data,method="w"):
	"""
	This function writes data to a csv file. You do not need to import the csv module to use this.
	Note that this will write and not append, meaning that it will override any data currently in the file.
	Inputs:
	filename: the name of the file
	data: the data to write. If left blank, will default to a blank row. Note that this is a list.
	method: the method can be either w for write or a for append. Defaults to w.
	Output:
	Returns 0 if everything went well, -1 if the file was not found or -2 if there was some other error.
	"""
#	if method.lower() != "w" or method.lower() != "a":
#		return -5
	if ".csv" not in filename:
		return -1
	try:
		file=open(filename,method)
	except:
		return -2
	writer=csv.writer(file)
	try:
		i=0
		while i<len(data):
			data[i]=str(data[i])
			i+=1
	except:
		return -3

	try:
		writer.writerow(data)
	except:
		return -4