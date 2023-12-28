import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service




#method 2
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/Owner/PycharmProjects/PythonSelmFrameWork/tests/chromedriver.exe")  #starting and stopping chromedriver from the path
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()


#METHOD 1 without using index
# cardItems = driver.find_elements(By.CSS_SELECTOR, "app-card")
# for item in cardItems:
#     print(item.find_element(By.CSS_SELECTOR, ".card-title").text)
#     if item.find_element(By.CSS_SELECTOR, ".card-title").text == "Blackberry":
#         item.find_element(By.CSS_SELECTOR, ".card-footer button").click()


#METHOD 2 with using index
# cardItems = driver.find_elements(By.CSS_SELECTOR, ".card-title")
# i = -1
# for item in cardItems:
#     i = i+1
#     print(item.text)
#     if item.text == "Blackberry":
#         print("ok")
#         # item.find_element(By.CSS_SELECTOR, ".card-footer button").click()
#         driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()



#METHOD 3 with using index  and driver
cardItems = driver.find_elements(By.CSS_SELECTOR, "app-card")
i = -1
for item in cardItems:
    i = i+1
    title = driver.find_elements(By.CSS_SELECTOR, ".card-title")[i].text
    print(title)
    if title == "Blackberry":
        driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()



driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
#
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
# driver.find_element(By.LINK_TEXT, "India").click()
#
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='checkbox checkbox-primary']")))
# driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#
# msg = driver.find_element(By.CLASS_NAME, "alert-success").text
# assert "Success! Thank you!" in msg
