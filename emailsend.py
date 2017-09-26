import smtplib
readMe=open('file.txt','r')
str=readMe.read()
while(str):
 
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login("your email id ", "your email id password")
 
 msg = "YOUR MESSAGE!"
 server.sendmail("your email id", "email id at which you want to send message", msg)
 server.quit()
readMe.close()
