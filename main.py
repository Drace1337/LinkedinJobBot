import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(os.envrion["URL"])

time.sleep(10)
signin_button = driver.find_element(By.LINK_TEXT, value="Zaloguj się")
signin_button.click()


time.sleep(10)
reject_button = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()


time.sleep(5)
email = driver.find_element(By.ID, value="username")
email.send_keys(os.environ["EMAIL"])
psw = driver.find_element(By.ID, value="password")
psw.send_keys(os.environ["PSW"])
psw.send_keys(Keys.ENTER)


time.sleep(5)
apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button")
apply.click()

time.sleep(5)
phone = driver.find_element(By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(os.environ["PHONE"])

submit = driver.find_element(By.CSS_SELECTOR, value="footer button")
submit.click()
