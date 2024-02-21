from appium import webdriver


def create_driver():
    try:
        host = '20.60.5.100:4723'
        url = ('http://' + host + '/wd/hub')
        cap = {"deviceName": "iPhone",
               "platformName": "ios",
               "udid": "00008030-001068CC1AF8202E",
               "bundleId": "growatt.Localdebug.com",
               "webDriverAgentUrl": "http://20.60.5.100:8100",
               "noRest": 'true',
               "usePrebuiltWDA": 'false',
               "useXctestrunFile": "false",
               "skipLogCapture": "true",
               "platformVersion": "16.4.1"
               }
        driver = webdriver.Remote(url, cap)
        return driver

    except Exception as msg:
        print("driver异常 -> {0}".format(msg))


