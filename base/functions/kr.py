
"""
python first
django second
your app and locals last
"""
from django.utils import timezone
from django.core.mail import send_mail
from Skywalker import settings
from base.models import KR
import qrcode


def create_kr(kr_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    kr_id_json = {'qr_id': kr_id}
    qr.add_data(kr_id_json)
    qr.make(fit=True)
    qr_img = qr.make_image()
    file_name = "qr" + str(kr_id) + ".jpg"
    qr_img.save(file_name)


def combine_images():
    pass


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
