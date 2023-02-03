from twilio.rest import Client

account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def alert_message(self, messages):
        message = self.client.messages.create(
            body=messages,
            from_="YOUR_TWILIO_NUMBER",
            to="YOUR_NUMBER"
        )
        print(message.sid)  # prints if successfully seng
