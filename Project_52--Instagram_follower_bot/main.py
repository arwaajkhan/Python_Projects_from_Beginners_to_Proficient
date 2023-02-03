from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

USER_NAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"


class InstaFollower:

    def __init__(self):
        s = Service("C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        # LOADING TIME FOR AUTHENTICATION
        sleep(5)
        username_field = self.driver.find_element(By.XPATH, '//input[@name="username"]')
        username_field.send_keys(USER_NAME)
        sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_field.send_keys(PASSWORD)
        sleep(2)
        password_field.send_keys(Keys.ENTER)
        sleep(5)

        # CONTROLLING TWO POPUPS OF SAME NAME AS "NOT NOW"
        for _ in range(2):
            save_info_button = self.driver.find_element(By.XPATH, '//*[text()="Not Now"]')
            save_info_button.click()
            sleep(3)

    def find_followers(self):

        # SEARCH BUTTON CLICK
        search_button_click = self.driver.find_element(By.XPATH, '//div[text()="Search"]//parent::div//parent::'
                                                                 'div[@class="x6s0dn4 x9f619 xxk0z11 x6ikm8r xeq5yr9 '
                                                                 'x1s85apg x1swvt13 xzzcqpx"]')
        search_button_click.click()
        sleep(1)
        search_input_field = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        search_input_field.send_keys("elonmuskoffiicial")
        sleep(3)

        # TWICE ENTER SO THAT THE FIRST APPEARED NAME WILL BE CLICKED AND OPENED
        for _ in range(2):
            search_input_field.send_keys(Keys.ENTER)
            sleep(1)
        sleep(5)

        # CLICKING ON ACCOUNT'S FOLLOWERS TAB
        follower_text = self.driver.find_element(By.XPATH, '//*[@class= "_aacl _aacp _aacu _aacx _aad6 _aade"]//'
                                                           'parent::a[@href="/elonmuskoffiicial/followers/"]')
        follower_text.click()

        sleep(5)

        # PROVIDING THE FULL-XPATH OF POP-UP WINDOW
        modal = self.driver.find_element(By.XPATH, '//html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/'
                                                   'div/div/div/div/div[2]/div/div/div[2]')
        # LOADING TOTAL FOLLOWING ACCOUNT OF TWO SCROLLS PAGE
        for _ in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self):
        # GETTING HOLD OF ALL THE BUTTONS REQUIRED TO FOLLOW
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8."
                                                                 "_abcm button")
        for button in all_buttons:
            try:
                button.click()
                sleep(2)
            # HANDLING EXCEPTION IF OCCURRED IF CLICKED ON THE FOLLOWED ACCOUNT ALREADY
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '//button[text()="Cancel"]')
                cancel_button.click()


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()

sleep(300)
