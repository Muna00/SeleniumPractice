from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#service = Service("C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver.exe")
#driver= webdriver.Chrome(service=service)

#driver = webdriver.Chrome()
driver = webdriver.Edge()



driver.get("https://opensource-demo.orangehrmlive.com/")

# Add an explicit wait for the username field to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)  # eta na dile ashe na kisu tai time baray load hoy



driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Passed")
else:
    print("Failed")


# Keep the browser open for as long as you like
time.sleep(100)  # Adjust the time as needed
