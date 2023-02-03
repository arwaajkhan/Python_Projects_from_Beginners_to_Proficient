from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


class Selenium:

    def __init__(self):

        chrome_path = "C:\Development\chromedriver.exe"
        s = Service(chrome_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        # FOR TRANSLATING THE PAGE INTO ENGLISH
        self.driver.execute_script("document.querySelector('html').setAttribute('lang', 'en')")
        self.driver.get("https://docs.google.com/forms/d/1RU6PUHwJ-cPOQTqRRPOOR6LFndu50UGkJ004XNqr4cg/edit")

    def filling_into_sheet(self, link, price, address):

        # PAGE RELOAD TIME
        sleep(2)
        address_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/'
                                                           'div/div[1]/div/div[1]/input')
        price_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                         'div/div[1]/div/div[1]/input')
        link_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                        'div/div[1]/div/div[1]/input')
        address_field.send_keys(address)
        price_field.send_keys(price)
        link_field.send_keys(link)
        sleep(1)
        submit_button = self.driver.find_element(By.XPATH, '//div[@role="button" and @jsname="M2UYVd"]')
        submit_button.click()
        # NEW FORM CLICK
        sleep(2)
        next_page = self.driver.find_element(By.XPATH, '//div[@class="c2gzEf"]/a')
        next_page.click()

