import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/78931bd35731db468b90fb1feb4e199d/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheet_value(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(self.destination_data)
        return self.destination_data

    def update_sheet_value(self):
        for city in self.destination_data:
            # Creating a parameter to be passed as a dictionary to the put request which contains the value of that
            # field name, and it holds the key which is singular form of last-word of api endpoint
            # for populating that field column
            sheet_input = {
                "price": {
                    # Column name : column value
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=sheet_input
            )
            print(response.text)

