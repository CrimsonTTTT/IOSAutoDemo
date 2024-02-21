import unittest

from myconfig.DriverConfig import create_driver


class UnitTestConfig(unittest.TestCase):
    """
    自定义每个方法的前置执行和后置执行
    """
    @classmethod
    def setUpClass(cls):
        print("运行setupClass")
        cls.driver = create_driver()
        # cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        print("运行tearDownClass")
        cls.driver.quit()

    # def setUp(self) -> None:
    #     print("setUp.....")
    #
    # def tearDown(self) -> None:
    #     print("tearDown.....")
