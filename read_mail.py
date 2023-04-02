import sensitive_data
from imap_tools import MailBox, AND
import os

# user and password to access the email. The password is the same gmail generate for us in first Configuration Step
user = sensitive_data.email
password = sensitive_data.password
directory = "C:/tmp/pypath/images/"

def create_path(directory):
    if not os.path.exists(directory):
        path = directory.split("/")
        dir = ""
        for folder in path:
            dir = dir + folder + '/'
            if not os.path.exists(dir):
                os.mkdir(dir)        

def transf_image():
    create_path(directory)
    for file in os.listdir():
        #or ".jpeg" or ".png"
        if ".jpg" in file.lower():
            print(file)
            os.rename(file, directory + file)

def readMail():
    with MailBox('imap.gmail.com').login(user, password) as myMailBox:
        for mail in myMailBox.fetch():
            if len(mail.attachments) > 0:
                for attach in mail.attachments:
                    with open(attach.filename, 'wb') as image:
                        image.write(attach.payload)
                        image.close

            return mail.subject, mail.text