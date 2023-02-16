import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Launching browser and opening website
@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.tescomobile.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


