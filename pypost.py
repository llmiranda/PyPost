from instagrapi import Client
import os
import sensitive_data

directory = "C:/tmp/pypath/images/"

cl = Client()
cl.login(sensitive_data.instagram_user, sensitive_data.instagram_pass)

def main (taged, text):
    for file in os.listdir(directory):
        #
        media = cl.photo_upload(directory + file, '@' + str(taged) + "\n" + str(text))
        os.remove(directory + file)