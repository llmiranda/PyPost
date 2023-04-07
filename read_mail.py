from imap_tools import MailBox, AND
import os
from random import randint
from time import sleep

import sensitive_data
import get_instagram_user
import pypost

# user and password to access the email. The password is the same gmail generate for us in first Configuration Step
user = sensitive_data.email
password = sensitive_data.password
directory = "C:/tmp/pypath/images/"
instagram_user = ""

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
        if file.split(".")[-1] in ("jpg" or "jpeg" or "png"):
            os.rename(file, directory + file)

def readMail():
    with MailBox('imap.gmail.com').login(user, password) as myMailBox:
        for mail in myMailBox.fetch():
            if len(mail.attachments) > 0:
                for attach in mail.attachments:
                    with open(attach.filename, 'wb') as image:
                        image.write(attach.payload)
                        image.close

            transf_image()
            instagram_user = get_instagram_user.main(mail.subject.lower())
            pypost.main(instagram_user, mail.text)
            myMailBox.delete(myMailBox.uids(AND(seen=True)))
            sleep(randint(30,300))