import time

import pytest


from TestData.HomepageDatas import HomePageDatas
from Utilities.BaseClass import Baseclass
from pageObjects.HomePage import HomePage



class TestHomePage(Baseclass):
    def test_homepageSubmition(self, getDatas):
        self.driver.implicitly_wait(3)
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Getting all names")
        homePage.getSendName().send_keys(getDatas["name"])
        log.info(getDatas["name"])

        homePage.getEmail().send_keys(getDatas["email"])
        log.info(getDatas["email"])

        homePage.getPassWrd().send_keys(getDatas["passcod"])
        time.sleep(2)

        homePage.getPassWrd().click()
        self.selectDropdown(homePage.getGender(), getDatas["gender"])

        homePage.getRadioBtn().click()

        homePage.getSubmtBtn().click()

        msg = homePage.getAlrtMsg().text
        time.sleep(2)
        print(msg)
        assert "successfully" in msg


        homePage.getTextInpt().send_keys(getDatas["msg"])

        homePage.getTextInpt().clear()

        homePage.getTextInpt().send_keys(getDatas["msg"])

        time.sleep(2)
        self.driver.refresh()

    @pytest.fixture(params=HomePageDatas.getExcelData("Testcase1"))
    def getDatas(self, request):
        return request.param


