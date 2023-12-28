from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(text(),'Shop')]")

    sendName = (By.CSS_SELECTOR, "input[name='name']")

    email = (By.NAME, "email")

    passwrd = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")

    radioBtn = (By.CSS_SELECTOR, "#inlineRadio1")

    submitBtn = (By.XPATH, "//input[@type='submit']")

    alrtMsg = (By.CLASS_NAME, "alert-success")

    textInpt = (By.XPATH, "(//input[@type='text'])[3]")




    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPageObj = CheckOutPage(self.driver)
        return checkOutPageObj

    def getSendName(self):
        return self.driver.find_element(*HomePage.sendName)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassWrd(self):
        return self.driver.find_element(*HomePage.passwrd)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadioBtn(self):
        return self.driver.find_element(*HomePage.radioBtn)

    def getSubmtBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getAlrtMsg(self):
        return self.driver.find_element(*HomePage.alrtMsg)

    def getTextInpt(self):
        return self.driver.find_element(*HomePage.textInpt)


