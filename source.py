import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import package as pg

listner = sr.Recognizer()
engine = pyttsx3.init()

#narrat the sentence that it recieve
def talk(text):
	engine.say(text)
	engine.runAndWait()


#listen and return the sentence 
def get_info():
	try:
		with sr.Microphone() as source:
			print('listning......')
			voice = listner.listen(source)
			info = listner.recognize_google(voice)
			print(info)
			return info.lower()

	except: 
		pass

#sending email to the reciever
def send_email(reciever,subject,message):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls() #tls = Transfer Layer Security
	#input the senders email and password from the package
	server.login(pg.email(),pg.password())
	email = EmailMessage()
	email['From']=pg.email()
	email['To']=reciever
	email['Subject']=subject
	email.set_content(message)
	server.send_message(email)


#Basic UI
def get_email_info():
	while (1):

		talk('to whom you want to send email')
		name=str(get_info())
		name = name.replace(" ", "")
		name = name.replace('dot','.')
		reciever= name+'@gmail.com'
		print(reciever) 
		talk('what is the subject of your email')
		subject=get_info()
		talk('tell me you message that you want to deliever')
		message=get_info()		
		print(reciever)
		talk('please confirm the email in yes or no')
		conformation = str(get_info())
		if conformation == 'yes':
			send_email(reciever,subject,message)
			talk('email sent')
		else :
			break
			
		#repeat the cycle if false
		talk('do you want to send more emails in yes or no')
		if get_info() == 'no':
			talk('thank you')
			break

	

get_email_info()