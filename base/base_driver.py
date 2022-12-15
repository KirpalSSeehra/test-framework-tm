import time

from selenium.webdriver.common.by import By
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

    def wait_until_invisibility_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        invisible_element = wait.until(EC.invisibility_of_element((locator_type, locator)))
        return invisible_element

    def click_execute_script(self):
        wait = WebDriverWait(self.driver, 20)
        click_execute = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_6')]")))
        self.driver.execute_script("arguments[0].click();", click_execute)
