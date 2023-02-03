from bs4 import BeautifulSoup
import requests

URL = "https://www.realtor.com/apartments/San-Francisco_CA/type-single-family-home/beds-1/baths-1/price-na-4050"

headers = {
    "User-Agent": "YOUR_DESKTOP_SPEC",
    "Accept-Language": "en-US"
}


class WebScraping:

    def __init__(self):
        self.response = requests.get(URL, headers=headers)
        self.realtor_contents = self.response.text
        self.soup = BeautifulSoup(self.realtor_contents, "html.parser")
        self.link_list = []
        self.price_list = []
        self.address_list = []
        self.houses_info = self.soup.find_all(name="div", class_="BasePropertyCard_propertyCardWrap__pblQC")
        self.list_of_all()

    def list_of_all(self):
        for house in self.houses_info:
            link = "https://www.realtor.com" + house.find(name="a").get("href")
            price = house.find(class_="Price__Component-rui__x3geed-0 ibnFqH card-price").text
            address = house.find(class_="card-address truncate-line").text
            self.link_list.append(link)
            self.price_list.append(price)
            self.address_list.append(address)

