#IMPORTANT
#Requires Python3
#Running the code below will only works with Yahoo
#Choosing different provider such as Gmail or Hotmail will require to get their SMTP setting and replace the below
#Will try updating the below to be more dynamic with other SMTP Servers
#Running the code below will not keep running, I use linux crontab to have this code scheduled to work every certain time

from requests import get
from datetime import date
import smtplib


ip = get('https://api.ipify.org').text           #will get the public IP
print ("My public IP address is:" + ip)          #for testing, this will print the IP
today = date.today()                             # to be used for the date when sending the email

def sendmail():        #function to send email
  
    fromMy = ('email_send_from') 
    to  = ('email_to_receive')
    subj=('Public IP')
    date=today
    message_text=ip

    msg = ("From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s") % ( fromMy, to, subj, date, message_text )
 
 #Add Yahoo email
    email = ('email')           #email should be between single quotation
 #Add Yahoo email password
    password = ('password')     #password should be between single quotation

    try :
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)         #SMTP link and port
        server.connect("smtp.mail.yahoo.com",587)                #SMTP link and port
        server.starttls()
        server.login(email,password)
        server.sendmail(fromMy, to, msg)
        server.quit()    
        print ('ok the email has been sent ')
    except SMTPException:
        print ('cant send the Email')

sendmail()
