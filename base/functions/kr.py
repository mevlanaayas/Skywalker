# -*- coding: utf-8 -*-
"""
python first
django second
your app and locals last
"""
import os
from email.mime.image import MIMEImage

from MyQR import myqr
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from Skywalker import settings
from base.templates.email_template import EMAIL_TEMPLATE


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


def send_kr(email_address, kr_id):
    file_name = "qr_" + str(kr_id) + ".png"
    subject = "Skywalker QR Code is created on " + str(timezone.localtime(timezone.now()))
    to_list = [email_address]
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.EMAIL_HOST_USER,
        to=to_list,
    )
    with open(file_name, 'rb') as fp:
        image = MIMEImage(fp.read())
    email.attach(image)
    html_content = EMAIL_TEMPLATE
    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=True)
    os.remove(file_name)
