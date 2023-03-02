import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Launching browser and opening website
@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.tescomobile.com/")
    driver.maximize_window()
    driver.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["tms.tescomobile.com"]})
    driver.execute_cdp_cmd('Network.enable', {})
    request.cls.driver = driver
    yield
    driver.close()


