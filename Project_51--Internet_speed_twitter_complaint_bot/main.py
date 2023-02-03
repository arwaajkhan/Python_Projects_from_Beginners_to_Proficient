from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

TWITTER_EMAIL = "YOUR_EMAIL"
TWITTER_PASSWORD = "YOUR_PASSWORD"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.s = Service("C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.down = None
        self.up = None
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[text()="Go"]')
        go_button.click()
        sleep(90)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
                                             ).text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
                                           ).text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(5)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                         'div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/'
                                                         'div/input')
        # ENTERING EMAIL
        sleep(1)
        email_field.send_keys(TWITTER_EMAIL)
        sleep(2)
        email_field.send_keys(Keys.ENTER)

        # ENTERING PASSWORD
        sleep(5)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                            'div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/'
                                                            'div/div[2]/div[1]/input')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        # WRITING TWEET
        sleep(10)
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                         'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                         'div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/'
                                                         'div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up " \
                f"when I pay for 50down/5up?"
        tweet_field.send_keys(tweet)
        sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                          'div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[3]/div/div/div[2]/div[3]')
        tweet_button.click()


internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()
sleep(300)
