import smtplib
import config
def send_email(subject,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        message="subject:{}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS,config.REMAIL_ADDRESS,message)
        server.quit()
        print("Sucess: Email sent!")
    except:
        print("Email failed to send.")
subject="Text subject"
msg="Hello buddy"
send_email(subject,msg)
