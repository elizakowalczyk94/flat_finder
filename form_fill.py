import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

FORM_URL = r"http://docs.google.com/forms/d/e/1FAIpQLSensmGNGsalUpAS8whkm8ESlOCKgwbIOa-RPA5y_iX8UM6UOw/viewform?usp=sf_link"
CHROME_DRIVER_PATH = r"C:\Users\Kowalczyk\PycharmProjects\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to avoid closing Chrome


class FormFill:

    def __init__(self):
        chrome_service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        self.driver.get(FORM_URL)

    def __goto_another_form(self):
        button = self.driver.find_element(by=By.LINK_TEXT, value="Prześlij kolejną odpowiedź")
        button.click()

    def fill_google_form(self, apartments_data_list):
        for apartment in apartments_data_list:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input.whsOnd.zHQkBf")))
            form_inputs = self.driver.find_elements(by=By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
            form_inputs[0].send_keys(apartment["address"])
            form_inputs[1].send_keys(apartment["price"])
            form_inputs[2].send_keys(apartment["url"])
            time.sleep(1)
            submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.NqnGTe")
            submit_button.click()
            time.sleep(1)
            self.__goto_another_form()
