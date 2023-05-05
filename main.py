import read_mail
import pypost

cl = pypost.loggin_user()
read_mail.readMail(cl)
print("Processamento encerrado")