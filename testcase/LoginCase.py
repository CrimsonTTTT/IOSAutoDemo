from myconfig.UnitTestConfig import UnitTestConfig
from pages.LoginPage import LoginPage


class TestLoginCase(UnitTestConfig):


    def test_engineer_login(self):
        LoginPage(self.driver).engineer_login("aaab8001", "123456")

