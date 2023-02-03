from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Selenium basic setup
s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Getting cookies hold
cookies = driver.find_element(By.ID, "cookie")

# Initialise the required timers
five_seconds_lap = time.time() + 10
five_minutes_lap = time.time() + 60 * 2

# Get hold of upgrade items' ids
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id_list = [item.get_attribute("id") for item in items]


while True:
    # infinite cookies click
    cookies.click()

    # check for every five seconds of interval
    if time.time() > five_seconds_lap:

        # getting all the b tags of price and text_part
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        price_list = []

        # filtering the price in integer value
        for price in prices:
            text_price = price.text
            # to avoid indexOutOfRange cuz the last element of price_list is empty
            if text_price != "":
                price_in_int = int(text_price.split("-")[1].strip().replace(",", ""))
                price_list.append(price_in_int)

        # my cookies(or money)
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Dictionary to store item id's and prices
        cookie_upgrade_dict = {}
        for i in range(len(price_list)):
            cookie_upgrade_dict[price_list[i]] = items_id_list[i]

        affordable_upgrades = {}
        # Comparing if upgradable and buying the expensive one
        for cost, id_name in cookie_upgrade_dict.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id_name

        high_price = max(affordable_upgrades)
        purchase_id = affordable_upgrades[high_price]
        driver.find_element(By.ID, purchase_id).click()

        # increase five_seconds timer
        five_seconds_lap = time.time() + 5

    if time.time() > five_minutes_lap:
        cookies_per_second = driver.find_element(By.ID, "cps").text
        new_value = cookies_per_second.split(":")[1]
        print(new_value)
        break


