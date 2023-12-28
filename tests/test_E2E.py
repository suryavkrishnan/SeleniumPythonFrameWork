import time

from Utilities.BaseClass import Baseclass

from pageObjects.HomePage import HomePage


class TestOne(Baseclass):
    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(3)
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all card titles")
        cardItems = checkOutPage.getCardItems()
        i = -1
        for item in cardItems:
            i = i + 1
            title = checkOutPage.getCardtitles()[i].text
            print(title)
            log.info(title)
            if title == "Blackberry":
                checkOutPage.getCardFooters()[i].click()

        checkOutPage.getCheckoutButton1().click()
        confirmPage = checkOutPage.getCheckoutButton2()


        time.sleep(5)

        log.info("Get country")
        confirmPage.getCountryInput().send_keys("India")

        self.varifyLinkPresence("India")

        confirmPage.getCountry().click()

        self.varifyCheckboxPresence()

        confirmPage.getCheckBox().click()

        confirmPage.getSubmit().click()

        msg = confirmPage.getAlertMsg().text
        log.info("assert msg is "+msg)
        assert "Success! Thank you!" in msg

