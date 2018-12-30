#inset your receiving and sending emails
#change the smtp protocol type to gmail or naver accordingly
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
    
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    
    msg['Subject'] = 'Fall Alert'
    msg['From'] = 'aaa@naver.com' #insert sending email
    msg['To'] = 'haliunetto@gmail.com' #insert receiving email
    
    text = MIMEText("Urgent: Fall Detected!!!")
    msg.attach(text)
    
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.naver.com', 587 ) #for naver emails
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('sedning email', 'PW') #add sending email and password
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
