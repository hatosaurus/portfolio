from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import os
import smtplib
from email.message import EmailMessage


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_KEY']
Bootstrap5(app)

MY_EMAIL = os.environ["MY_EMAIL"]
MY_EMAIL_PASSWORD = os.environ["MY_EMAIL_PASSWORD"]
TARGET_EMAIL = os.environ["TARGET_EMAIL"]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/portfolio')
def portfolio():
    portfolio = [1, 2, 3, 4, 5, 6, 7, 8]
    return render_template("portfolio.html", portfolio=portfolio)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", form_submitted=True)
    else:
        return render_template("contact.html", form_submitted=False)


def send_email(name, email, phone, message):
    smtp_server = 'mail.privateemail.com'
    port = 465
    login = MY_EMAIL
    password = MY_EMAIL_PASSWORD
    email_message = EmailMessage()
    email_message["Subject"] = "New Message Received"
    email_message["From"] = MY_EMAIL
    email_message["To"] = TARGET_EMAIL
    content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    email_message.set_content(content)
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(login, password)
    server.send_message(email_message)
    server.quit()


if __name__ == "__main__":
    app.run(debug=True)