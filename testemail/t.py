
import smtplib
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
connection.login('mansikumawat42137@gmail.com','gpnj umbu kvvv kcnp')
connection.sendmail('mansikumawat42137@gmail.com','aniketsirota64','subject: this is the subject \n\n hello user')
print("Email sent")
connection.quit()
