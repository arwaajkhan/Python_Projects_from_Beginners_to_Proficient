from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_sheet_value()
# print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for value in sheet_data:
        value["iataCode"] = flight_search.get_iatacode(value["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data  # This program worked even without this line of code
    data_manager.update_sheet_value()

# This code works for dateutil.relativedelta
# date = datetime.now()
# today_date = date.strftime("%d/%m/%Y")
# next_date = (date + relativedelta(months=+6)).strftime("%d/%m/%Y")

tomorrow_date = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_after_date = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow_date,
        to_time=six_month_after_date
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.alert_message(
            messages=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                     f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date}"
                     f" to {flight.return_date}."
        )



