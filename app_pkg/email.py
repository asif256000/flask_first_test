# Can also use multiprocessing here, but it takes up more resources.
# This is not much required only for sending mails.
from threading import Thread

from flask import current_app
from flask_mail import Message

from app_pkg import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body, attachments=None, sync=False):
    # sender=sender -> causing error: smtplib.SMTPDataError:
    # (550, b'The from address does not match a verified Sender Identity.
    # Mail cannot be sent until this error is resolved.
    # Visit https://sendgrid.com/docs/for-developers/sending-email/sender-identity/
    # to see the Sender Identity requirements')
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)

    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
