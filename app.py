import logging
import pytz
from datetime import datetime
from smtplib import SMTPException

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from loggers import setup_logging
from utils import sent_email

setup_logging()
log = logging.getLogger(__name__)

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/index/')
def main_page():
    return render_template('main.html')


@app.route('/cennik/')
def price():
    return render_template('price.html')


@app.route('/sluzby-uctovnictvo/')
def service_accounting():
    return render_template('service_accounting.html')


@app.route('/sluzby-dane/')
def service_tax():
    return render_template('service_tax.html')


@app.route('/sluzby-mzdy/')
def service_sallary():
    return render_template('service_sallary.html')


@app.route('/kontakty/')
def contact():
    return render_template('contact.html', email_sent=False)


@app.route('/form_data', methods=['POST'])
def form_data():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    text = request.form['text']

    now = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now(pytz.timezone('Europe/Bratislava')))
    form = f"Cas: {now}\nMeno: {name}\nTelefon: {phone}\nEmail: {email}\nText: {text}\n"

    try:
        sent_email(form, now)
    except SMTPException:
        log.error("Failed to sent form email %r" % form, exc_info=True)
        return render_template('contact.html', email_sent=False)

    log.info("Form email was sent successfully: %r" % form)
    return render_template('contact.html', email_sent=True)


if __name__ == '__main__':
    app.run()
