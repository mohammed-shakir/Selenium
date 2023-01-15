class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "Web" in self.driver.title