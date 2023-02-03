import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/JBL-Portable-Wireless-Powerful-Black/dp/B01MSYQWNY/ref=sr_1_5?keywords=jbl+speaker+" \
      "bluetooth&qid=1672490355&sprefix=jbl+speaker%2Caps%2C723&sr=8-5"
headers = {
    "Accept-Language": "en-US",
    "User-Agent": "YOUR_DESKTOP_SPECIFICATION"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
price_value = soup.find(name="span", class_="a-price-whole")
price = float(price_value.getText().replace(",", ""))
# print(price)


my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

if price < 5000:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="SENDER_EMAIL",
        msg="Subject:Amazon-Price-Tracker-alert\n\nAlert!! The price of the JBL speaker is less than ₹5000/-"
    )
