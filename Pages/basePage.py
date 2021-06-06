from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import secrets


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find(self, element_data):
        wait = WebDriverWait(self.driver, 15)
        find_method = element_data[0]
        locator = element_data[1]
        if find_method.upper() == 'XPATH':
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return self.driver.find_element(By.XPATH, locator)
        elif find_method.upper() == 'CSS_SELECTOR':
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        elif find_method.upper() == 'CLASS_NAME':
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            return self.driver.find_element(By.CLASS_NAME, locator)
        elif find_method.upper() == 'ID':
            wait.until(EC.visibility_of_element_located((By.ID, locator)))
            return self.driver.find_element(By.ID, locator)
        else:
            raise Exception("Can't find such finding method.")

    def wait_for_element_to_appear(self, element_data):
        wait = WebDriverWait(self.driver, 15)
        find_method = element_data[0]
        locator = element_data[1]
        if find_method.upper() == 'XPATH':
            return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        elif find_method.upper() == 'CSS_SELECTOR':
            return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        elif find_method.upper() == 'CLASS_NAME':
            return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
        elif find_method.upper() == 'ID':
            return wait.until(EC.visibility_of_element_located((By.ID, locator)))
        else:
            raise Exception("Can't find such finding method.")

    def click(self, element):
        elem = self.find(element)
        elem.click()

    def type_text(self, element, text):
        element.send_keys(text)

    def generate_random_value(self, length):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
