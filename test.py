from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

def test_edge():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    driver.implicitly_wait(3)

    text_box = driver.find_element(By.NAME, "my-text")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(By.ID, "message")
    value = message.text

    if value == "Received!":
        print("Test passed")
    else:
        print("Test failed")

    driver.quit()

test_edge()