# import smtplib
# import traceback
#
# gmail_user = 'mansikumawat42137@hmail.com'
# gmail_password = 'koxq bxgh ptwq exea'
#
# sent_from = gmail_user
# to = ['aniketsirota64@gmail.com', 'agrawalanant.908@gmail.com']
# subject = 'This is my first Python Message'
# body = 'Hi, What is going on'
#
# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, body)
#     server.close()
#     print('Email sent!')
#
# except:
#     traceback.print_exc()


import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login('mansikumawat42137@gmail.com', 'gpnj umbu kvvv kcnp')
connection.sendmail('mansikumawat42137@gmail.com', 'gandhwanigautam@gmail.com',
                    'subject: this is the subject \n\n hello user')
print("Email sent")
connection.quit()
