
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


USERNAME = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/")
driver.maximize_window()

# #ACCEPT COOKIES
time.sleep(10)
cookies = driver.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()
time.sleep(1)

# LOGIN CLICK
login_button = driver.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(5)

# CHOOSE OPTION FACEBOOK
facebook_click = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[2]/'
                                               'button')
facebook_click.click()
time.sleep(5)

# ENTERING INTO FACEBOOK POP-UP WINDOW
base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

# FILLING FACEBOOK CREDENTIAL
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(USERNAME)
time.sleep(2)
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(PASSWORD)
time.sleep(2)
password_field.send_keys(Keys.ENTER)
# time.sleep(10)

# SWITCHING BACK TO BASE WINDOW
driver.switch_to.window(base_window)

# REMOVING POP-UPS INSIDE TINDER
# ALLOW LOCATION
time.sleep(15)
allow_button = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[1]')
allow_button.click()
time.sleep(2)
# DISALLOW NOTIFICATION
not_interested_button = driver.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div/div/div[3]/button[2]')
not_interested_button.click()
time.sleep(10)

# SWITCHING THE DARK MODE
dark_mode_button = driver.find_element(By.ID, 'darkModeSwitch')
dark_mode_button.click()


# CLOSING THE POP-UP WINDOWS [didn't work cuz the element_path is hidden]
closing_dark_mode_popup = driver.find_element(By.XPATH, '//div/button[@aria-hidden="false"]')
closing_dark_mode_popup.click()


# LIKING AUTOMATICALLY
for _ in range(4):

    # ADDING TIMER TO LOAD ANOTHER PROFILE
    time.sleep(3)
    try:
        like_button = driver.find_element(By.XPATH, '//button[@draggable="false"]//parent::div[@class="Mx(a) Fxs(0)'
                                                    ' Sq(70px) Sq(60px)--s Bd Bdrs(50%)'
                                                    ' Bdc($c-ds-border-gamepad-like-default)"]')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(5)


time.sleep(120)
driver.quit()
