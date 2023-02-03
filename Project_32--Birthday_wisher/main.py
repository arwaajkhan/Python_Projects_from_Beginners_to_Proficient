
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

today = dt.datetime.now()

df = pd.read_csv("birthdays.csv")
value = df[(df.day == today.day) & (df.month == today.month)]
result = value["name"].to_string(index=False)

ran = random.randint(1, 3)
with open(f"letter_templates/letter_{ran}.txt") as data_file:
    contents = data_file.read()
    birthday_file = contents.replace("[NAME]", result)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="SENDER_GMAIL",
                            msg=f"Subject:Birthday_Wish\n\n{birthday_file}")

