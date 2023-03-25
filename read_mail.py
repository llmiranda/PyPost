import sensitive_data
from imap_tools import MailBox, AND
import os

# user and password to access the email. The password is the same gmail generate for us in first Configuration Step
user = sensitive_data.email
password = sensitive_data.password
directory = "C:/tmp/images/"

"""def create_path(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    #
    os.chdir(directory)
    print(os.getcwd())"""

def readMail():
    with MailBox('imap.gmail.com').login(user, password) as myMailBox:
        for mail in myMailBox.fetch():
            if len(mail.attachments) > 0:
                for attach in mail.attachments:
                    with open(attach.filename, 'wb') as image:
                        #create_path(directory)
                        image.write(attach.payload)


            """print(f"From: {mail.from_}")
            print(f"Attachment: {mail.attachments}")
            print(f"Date: {mail.date}")
            print(f"Subject: {mail.subject}")
            print(f"Text: {mail.text}")"""
            #print(mail.from_, mail.attachments, mail.date, mail.subject, len(mail.text or mail.html))