import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR_API_KEY"

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "demo"
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]

new_list = [value["4. close"] for (key, value) in data.items()]

comparing_price = list(map(float, new_list))
difference = comparing_price[0] - comparing_price[1]

percentage = round((difference / comparing_price[0]) * 100)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# if comparing_price[0] > comparing_price[1]:
#     value = comparing_price[0]
#     percentage = (difference/value)*100
# else:
#     decrement = comparing_price[1]
#     value = comparing_price[1]
#     percentage = (difference / value) * 100


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(percentage) > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME

    }
    new_response = requests.get(url=NEWS_API, params=news_parameters)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    formatted_article = [f"{STOCK}: {up_down}{percentage}%\nHeadline: {article['title']} \n {article['description']}"
                         for
                         article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="YOUR_TWILIO_NUMBER",
            to="YOUR_NUMBER"
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
