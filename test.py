from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import unittest

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    def test_example(self):
        self.driver.implicitly_wait(3)

        text_box = self.driver.find_element(By.NAME, "my-text")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = self.driver.find_element(By.ID, "message")
        value = message.text

        if value == "Received!":
            print("Test passed")
        else:
            print("Test failed")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()