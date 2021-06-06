import pytest
from selenium import webdriver
from Configs.config import TestData
from Pages.registration_popup import RegistrationPopup
from Pages.top_dashboard import TopDashboard


@pytest.fixture()
def driver():
    d = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    d.maximize_window()
    d.get(TestData.BASE_URL)
    yield d
    d.quit()


@pytest.fixture()
def registration_popup(driver):
    return RegistrationPopup(driver)


@pytest.fixture()
def dashboard(driver):
    return TopDashboard(driver)
