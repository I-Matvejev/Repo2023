import datetime
import pandas as pd
from email.message import EmailMessage
from email.utils import make_msgid
import smtplib
import os
import random


current_day_month = datetime.date.today().strftime('%d.%m')


def email_no_birthday():
    sender = ""  # enter sender's email
    recipient = ""  # enter recipients' emails

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Именинники"
    email.set_content(f"Сегодня - {current_day_month} - именинников нет.")

    with smtplib.SMTP("server", port=25) as server:  # put server instead of "server"
        server.sendmail(sender, recipient, email.as_string())


def email_to_birthday_children(mail, name, gender, f_name):
    sender = ""  # enter sender's email
    recipients = mail, ""  # enter recipients' emails

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipients
    email["Subject"] = f"С днём рождения, {name}!"

    if gender == 'M':
        figure_id = make_msgid()
        email.add_alternative("""
        <!DOCTYPE html>
        <html>
          <head></head>
          <body>
            <p>Уважаемый""" + " " + str(name) + " " + str(f_name) + """,<br>коллектив ____
             от всей души поздравляет Вас с днём рождения!</p>
            <img src="cid:{figure_id}" />
          </body>
        </html>
        """.format(figure_id=figure_id[1:-1]), subtype='html')

    else:
        figure_id = make_msgid()
        email.add_alternative("""
        <!DOCTYPE html>
        <html>
          <head></head>
          <body>
            <p>Уважаемая""" + " " + str(name) + " " + str(f_name) + """,<br>коллектив ____
             от всей души поздравляет Вас с днём рождения!</p>
            <img src="cid:{figure_id}" />
          </body>
        </html>
        """.format(figure_id=figure_id[1:-1]), subtype='html')

    # get a random picture from directory and insert into html body
    img_dir = ""  # images' directory
    img_file = random.choice(os.listdir(img_dir))

    with open(os.path.join(img_dir, img_file), 'rb') as img:
        email.get_payload()[0].add_related(img.read(), 'image', 'jpg', cid=figure_id)

    with smtplib.SMTP("server", port=25) as server:  # put server instead of "server"
        server.sendmail(sender, recipients, email.as_string())


def check_for_birthday_children():
    # read in excel and compare the dates to check, if today is someone's birthday
    birthdays = pd.read_excel('file', sheet_name='prog')  # birthdays' file instead of 'file'
    birthday_dates = birthdays['birthday']
    birthday_dates_formatted = [i.strftime('%d.%m') for i in birthday_dates]
    birthday_children = {}

    # put all birthday children into a dictionary
    enum_dates = enumerate(birthday_dates_formatted)
    for j, i in enum_dates:
        if i == current_day_month:
            birthday_children[j] = [birthdays["first_name"][j], birthdays["last_name"][j],
                                    birthdays["e-mail"][j], birthdays["father's_name"][j], birthdays["gender"][j]]
    if birthday_children:
        # pass out the values for each birthday child to the send mail function
        for key in birthday_children:
            email_to_birthday_children(birthday_children[key][2], birthday_children[key][0],
                                       birthday_children[key][4], birthday_children[key][3])
    else:
        email_no_birthday()


check_for_birthday_children()
