import smtplib

sender = 'lvb999997@gmail.com'
res = 'vibritannia59@gmail.com'
pas = input(str("enter the password: "))
msg = "Subject: Python msg.\nTHIS email sent by python"

server = smtplib.SMTP('smtp.gmail.com', 587) #the port num
server.starttls()
server.login(sender, pas)
print("Login succccc")

server.sendmail(sender, res, msg)
print("email has been sent to: ", res)
server.quit()

#jaxi moak jzpx qcjs

#في الرسائل غير المرغوبة!