import read_mail
import get_instagram_user

subject = ""
email = ""
instagram_user = ""

subject, email = read_mail.readMail()

read_mail.transf_image()

instagram_user = get_instagram_user.main(subject)

print(instagram_user)

#print(subject)
#print(email)
