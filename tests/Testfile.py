import time

from SeleniumFrameWork.base.DriverClass import WebDriverClass
import SeleniumFrameWork.utilities.CustomLogger as cl
from SeleniumFrameWork.base.BasePage import BaseClass


wd = WebDriverClass()

driver = wd.getWebDriver('chrome')
bp = BaseClass(driver)

bp.launchApp('http://www.dummypoint.com/seleniumtemplate.html', 'Selenium Template — DummyPoint')

bp.sendText('Somesh', 'user_input', 'ID')
bp.clickElement('Form', 'LINK')

time.sleep(2)
driver.quit()
