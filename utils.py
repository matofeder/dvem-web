import smtplib

import config

EMAIL_FROM = config.EMAIL_FROM
EMAIL_FROM_PASS = config.EMAIL_FROM_PASS

EMAIL_TO = config.EMAIL_TO


def sent_email(form, time):
    email = '\r\n'.join([
        'To: %s' % ", ".join(EMAIL_TO),
        'From: %s' % EMAIL_FROM,
        'Subject: DVEM FORMULAR %s' % time,
        '', form
    ])
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_FROM_PASS)
    server.sendmail(EMAIL_FROM, EMAIL_TO, email)
    server.quit()

