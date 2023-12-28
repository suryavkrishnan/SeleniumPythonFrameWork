from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    countryInput = (By.XPATH, "//input[@id='country']")

    country = (By.LINK_TEXT, "India")

    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    submitBut = (By.XPATH, "//input[@type='submit']")

    alertMsg = (By.CLASS_NAME, "alert-success")

    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submitBut)

    def getAlertMsg(self):
        return self.driver.find_element(*ConfirmPage.alertMsg)