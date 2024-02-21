# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from appium import webdriver
from appium.webdriver.common.mobileby import By

from myconfig.LogConfig import Log


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

host = "20.60.5.100"
url = 'http://20.60.5.100:4723/wd/hub'
desired_caps = {"deviceName": "iPhone",
                "platformName": "ios",
                "udid": "00008030-001068CC1AF8202E",
                "bundleId": "growatt.Localdebug.com",
                "webDriverAgentUrl": "http://20.60.5.100:8100",
                "noRest": True,
                "usePrebuiltWDA": False,
                "useXctestrunFile": False,
                "skipLogCapture": True,
                "platformVersion": "16.4.1"
                }
driver = webdriver.Remote(url, desired_caps)
driver.find_element(By.ID, "YWLogUN").click()
log = Log()
log.debug("success action auto test.")


