import time

from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
    chkoutItems = (By.CSS_SELECTOR, "app-card")

    cardTitle = (By.CSS_SELECTOR, ".card-title")

    itemFooter = (By.CSS_SELECTOR, ".card-footer button")

    chkoutButton1 = (By.XPATH, "//a[contains(text(),'Checkout')]")

    chkoutButton2 = (By.XPATH, "//button[contains(text(),'Checkout')]")


    def getCardItems(self):
        return self.driver.find_elements(*CheckOutPage.chkoutItems)

    def getCardtitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.itemFooter)

    def getCheckoutButton1(self):
        return self.driver.find_element(*CheckOutPage.chkoutButton1)
    def getCheckoutButton2(self):
         self.driver.find_element(*CheckOutPage.chkoutButton2).click()
         time.sleep(5)
         confirmPageObj = ConfirmPage(self.driver)
         return confirmPageObj
