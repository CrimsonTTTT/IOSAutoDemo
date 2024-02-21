from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from myconfig.LogConfig import Log

log = Log()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        单个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    def find_elements(self, *loc):
        """
        多个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    # 重写定义send_keys方法
    def send_key(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            log.error("%s 页面中未能找到 %s 元素" % (self, loc))
