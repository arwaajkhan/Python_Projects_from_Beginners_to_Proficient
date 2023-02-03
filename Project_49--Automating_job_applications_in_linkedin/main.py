from selenium import webdriver
# from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "YOUR_EMAIL"
ACCOUNT_PASSWORD = "YOUR_PASSWORD"
PHONE = 1234567890

s = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3409094175&geoId=100665265&keywords=python%20developer&"
           "location=Kathmandu%2C%20B%C4%81gmat%C4%AB%2C%20Nepal&refresh=true")
driver.maximize_window()

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# AUTHORIZATION WHILE LOGGING INTO LINKEDIN
user_name_field = driver.find_element(By.ID, "username")
user_name_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# GETTING ID'S OF ALL THE JOB_LIST TO BE APPLIED IN A LIST
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
applying_jobs_list = [job.get_attribute("id") for job in jobs_list]
modified_job_list = [job for job in applying_jobs_list if job != ""]
# testing = driver.find_element(By.ID, modified_job_list[2])
# testing.click()

for job_id in modified_job_list:
    apply = driver.find_element(By.ID, job_id)
    apply.click()
    time.sleep(5)

    try:
        # GET CLICK OF EASY APPLY OPTION
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button .artdeco-button__text")
        if easy_apply.text == "Easy Apply":
            easy_apply.click()
            # FILLING CREDENTIALS WHILE APPLYING AND SUBMITTING
            phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
            if phone.text == "":
                phone.send_keys(PHONE)

            exiting_click = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal button")
            exiting_click.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            time.sleep(2)

        # submit = driver.find_element(By.CSS_SELECTOR, "footer button")
        # submit.click()

    except NoSuchElementException:
        print("No EASY-APPLY option was found")


time.sleep(120)
