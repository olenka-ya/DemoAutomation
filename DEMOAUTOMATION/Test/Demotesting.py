import unittest
import time
import HtmlTestRunner
#from DEMOAUTOMATION import myReports
from DEMOAUTOMATION.Driver.driver import chromedriver
from DEMOAUTOMATION.PagesDemo.Homepage import HomePage
from DEMOAUTOMATION.PagesDemo.Registerpage import RegisterPage
from DEMOAUTOMATION.screenshot import screen
from DEMOAUTOMATION.PagesDemo.Order import OrderPage


class MyTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver  #webdriver.Chrome(executable_path="C:/Users/Olga/PycharmProjects/SeleniumIntroduction/DEMOAUTOMATION/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test1_sign_up(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/")
        driver.implicitly_wait(5)
        homepage = HomePage(driver)
        homepage.click_sign_up()
        driver.implicitly_wait(5)
        reg = RegisterPage(driver)
        reg.enter_firstname("Olga")
        reg.enter_lastname("Ko")
        reg.enter_adress("22 Carluke Cres")
        reg.enter_email("olga@gmail.com")
        reg.enter_phone("4161112233")
        reg.click_female()
        reg.click_cricket()
        reg.select_language()
        reg.select_skills()
        reg.select_countries1()
        reg.select_countries2()
        reg.select_year()
        reg.select_month()
        reg.select_day()
        reg.enter_password("Testpass1")
        reg.confirm_password("Testpass1")
        reg.click_submit()
        #driver.implicitly_wait(20)
        driver.get_screenshot_as_file("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/DEMOAUTOMATION/screenshot/scrn.png")

    def test2_order(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("http://practice.automationtesting.in/")
        order = OrderPage(driver)
        order.click_practice_page()
        driver.implicitly_wait(5)
        order.click_add_to_cart()
        order.click_cart()
        driver.get_screenshot_as_file("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/DEMOAUTOMATION/screenshot/scrn1.png")
        order.click_checkout()
        order.enter_firstname("Olga")
        order.enter_lastname("Ko")
        order.enter_company_name("CACC")
        order.enter_email("olga@gmail.com")
        order.enter_phone("4161112233")
        order.select_country()
        order.enter_adress("22 Carluke Cres")
        order.enter_city()
        order.select_province()
        order.enter_postalcode("M2M2L2")
        order.select_payment()
        order.place_order()
        #driver.implicitly_wait(20)
        #driver.get_screenshot_as_file("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/DEMOAUTOMATION/screenshot/scrn2.png")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

