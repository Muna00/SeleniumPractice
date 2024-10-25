import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver= webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")


# Add an explicit wait for the username field to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Email"))
)  # eta na dile ashe na kisu tai time baray load hoy

driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")

driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")

driver.find_element(By.CLASS_NAME,"login-button").click()

act_title= driver.title
exp_title= "Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Passed")
else:
    print("Failed")

time.sleep(100)