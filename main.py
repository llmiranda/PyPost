import sensitive_data
from imap_tools import MailBox, AND

# user and password to access the email. The password is the same gmail generate for us in first Configuration Step
user = sensitive_data.email
password = sensitive_data.password

with MailBox('imap.gmail.com').login(user, password) as myMailBox:
    for mail in myMailBox.fetch():
        print(f"From: {mail.from_}")
        print(f"Attachment: {mail.attachments}")
        print(f"Date: {mail.date}")
        print(f"Subject: {mail.subject}")
        print(f"Text: {mail.text}")
        #print(mail.from_, mail.attachments, mail.date, mail.subject, len(mail.text or mail.html))