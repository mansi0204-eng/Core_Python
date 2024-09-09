import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "mansikumawat42137@gmail.com"
toaddr = "aniketsirota64@gmail.com"

msg = MIMEMultipart()  # instance of MIMEMultipart
msg['From'] = fromaddr  # storing the senders email address
msg['To'] = toaddr  # storing the receivers email address
msg['Subject'] = "This is the document attached"  # storing the subject
body = "Below is the Attachment"  # string to store the body of the mail
msg.attach(MIMEText(body, 'plain'))  # attach the body with the msg instance
filename = "file_name_with_extension"
attachment = open("C:/Users/Dell/Desktop/hello/emp.txt", "rb")  # open the file to be sent
p = MIMEBase('application', 'octet-stream')  # instance of MIME Base and named as P
p.set_payload((attachment).read())  # to change the payload into encoded form
encoders.encode_base64(p)  # encoded into base 64
p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
msg.attach(p)  # attach the instance 'p' to instance 'msg'
s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session
s.starttls()  # start TLS for security
s.login(fromaddr, "gpnj umbu kvvv kcnp")  # Authentication
text = msg.as_string()  # converts a multipart msg into a string
s.sendmail(fromaddr, toaddr, text)  # sending the email
s.quit()  # terminating the session
