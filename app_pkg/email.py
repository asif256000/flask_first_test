from flask import current_app
from flask_mail import Message
from app_pkg import mail
# Can also use multiprocessing here, but it takes up more resources.
# This is not much required only for sending mails.
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, recipients=recipients) #sender=sender, ???
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
