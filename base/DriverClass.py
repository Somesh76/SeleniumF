from selenium import webdriver
import SeleniumFrameWork.utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome("")
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            pass
        elif browserName == "firefox":
            pass
            self.log.info("FireFox Driver is initializing")

        return driver
