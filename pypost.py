from instagrapi import Client
import logging
import os
import sensitive_data
import image_rotate

directory = "C:/tmp/pypath/images/"

logger = logging.getLogger()

def loggin_user():
    cl = Client()
    cl.delay_range = [1, 3]
    
    try:
        session = cl.load_settings("session.json")
    except:
        #cl = Client()
        cl.login(sensitive_data.instagram_user, sensitive_data.instagram_pass)
        cl.dump_settings("session.json")
        session = cl.load_settings("session.json")

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(sensitive_data.instagram_user, sensitive_data.instagram_pass)

            #check if session is valid
            try:
                cl.get_timeline_feed()
            except:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()
                
                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(sensitive_data.instagram_user, sensitive_data.instagram_pass)
                cl.dump_settings("session.json")
            
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % sensitive_data.instagram_user)
            if cl.login(sensitive_data.instagram_user, sensitive_data.instagram_pass):
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

    return cl

def main (taged, text, client):
    for file in os.listdir(directory):
        #
        image_rotate.rotate(directory + file)
        #
        media = client.photo_upload(directory + file, '@' + str(taged) + "\n" + str(text))
        os.remove(directory + file)
        