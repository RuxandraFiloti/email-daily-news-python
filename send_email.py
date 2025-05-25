import smtplib, ssl
import os 

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "adaflori0207@gmail.com"
   # password = "ombj tdaf ktld nisz" 
    password = os.environ.get("PASSWORD") #find it in environment variables

    receiver = "adaflori0207@gmail.com"
    context = ssl.create_default_context()

   
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
