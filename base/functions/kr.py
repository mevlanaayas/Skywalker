
"""
python first
django second
your app and locals last
"""
import os
from MyQR import myqr
from django.utils import timezone
from django.core.mail import send_mail
from Skywalker import settings


def create_kr(kr_id):
    file_name = "qr_" + str(kr_id) + ".png"
    myqr.run(
        str(kr_id),
        version=settings.QR_CODE_DETAIL_VERSION,
        level='H',
        picture=os.getcwd() + '/square.jpg',
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=file_name,
        save_dir=os.getcwd()
    )


def send_kr(email, mg_id):
    subject = "Skywalker QR Code on " + str(timezone.localtime(timezone.now()))
    from_email = settings.MAIL_ADDRESS
    message = "general kenobi " + str(mg_id)
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

    # TODO: mail gönderme işleminden sonra dosyanın silinmesi
    """
    file_name = "qr" + str(mg_id) + ".jpg"

    with open(file_name, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    """
