import requests
from twilio.rest import Client

parameters = {
    "lat": 26.452475,
    "lon": 87.271782,
    "appid": "fed86984d9384ba559d465a7f376cd95",
    "exclude": "current,minutely,daily"
}

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_='YOUR_TWILIO_NUMBER',
        to='YOUR_NUMBER'
    )
    print(message.status)
