import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)


    def page_zoom(self):
        pageZoom = self.driver.execute_script("document.body.style.zoom= '67%'")


    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        clickable_element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return clickable_element

