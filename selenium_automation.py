import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_fail_login(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("invalid-standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("invalid-secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3').text

        self.assertIn('do not match', response_message)

    def test_b_success_login(self): 
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(3)

        response_message = browser.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span').text

        self.assertIn('PRODUCTS', response_message)
    
    def test_c_add_product_to_cart(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').text

        self.assertIn('Sauce Labs', response_message)
    
    def test_d_remove_product_from_cart(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="remove-sauce-labs-backpack"]').click()
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,'//*[@id="cart_contents_container"]/div/div[1]/div[3]').text

        self.assertNotIn('Sauce Labs', response_message)

    def test_e_sort_product_low_to_high(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,'//*[@id="item_2_title_link"]/div').text

        self.assertEqual('Sauce Labs Onesie', response_message)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()