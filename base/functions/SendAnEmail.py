import pyqrcode
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def createQrCode():
    big_code = pyqrcode.create('YOUR MESSAGE') #error='L', version=27, mode='binary'
    big_code.png('code.png', scale=6)

def sendAnEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ENTER MAIL ADDRESS", "PASSWORD")

    msg = MIMEMultipart()
    msg['Subject'] = "Skywalker QR Code"
    msg['From'] = "skywalkernav@gmail.com"
    msg['To'] = "furkanakan@gmail.com" #clientEmailAddress

    with open("code.png", 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

    server.send_message(msg)
    server.quit()

def sendUniqueQrCode(clientEmailAddress):
    createQrCode()
    sendAnEmail()

sendAnEmail()