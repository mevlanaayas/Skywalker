from base.constants.credentials import *
from base.models import KR
import qrcode
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def create_kr(kr_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(kr_id)
    qr.make(fit=True)
    qr_img = qr.make_image()
    file_name = "qr" + str(kr_id) + ".jpg"
    qr_img.save(file_name)


def combine_images():
    pass


def send_kr(email, id):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MAIL_ADDRESS, MAIL_PASSWORD)

    msg = MIMEMultipart()
    msg['Subject'] = "Skywalker QR Code"
    msg['From'] = "skywalkernav@gmail.com"
    msg['To'] = email

    # TODO: mail gönderme işleminden sonra dosyanın silinmesi

    file_name = "qr" + str(id) + ".jpg"

    with open(file_name, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

    server.send_message(msg)
    server.quit()

