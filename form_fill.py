import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv("venv/.env")

FORM_URL = r"http://docs.google.com/forms/d/e/1FAIpQLSensmGNGsalUpAS8whkm8ESlOCKgwbIOa-RPA5y_iX8UM6UOw/viewform?usp=sf_link"
LOGIN_URL = r"https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSensmGNGsalUpAS8whkm8ESlOCKgwbIOa-RPA5y_iX8UM6UOw%2Fviewform%3Ffbzx%3D-7373451500591819066&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
CHROME_DRIVER_PATH = r"C:\Users\Kowalczyk\PycharmProjects\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to avoid closing Chrome


class FormFill:

    def __init__(self):
        chrome_service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        self.driver.get(FORM_URL)
        self.user_email = os.getenv("EMAIL")
        self.user_pswrd = os.getenv("PASSWORD")

    def __goto_another_form(self):
        button = self.driver.find_element(by=By.LINK_TEXT, value="Prześlij kolejną odpowiedź")
        button.click()

    def __wait_for_elem(self, css_value: str):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_value)))

    def login(self):
        # Cannot login because of Google security system!
        self.driver.get(LOGIN_URL)
        self.__wait_for_elem("input.whsOnd.zHQkBf")
        email_input = self.driver.find_element(by=By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
        email_input.send_keys(self.user_email)
        email_input.send_keys(Keys.ENTER)

    def fill_google_form(self, apartments_data_list):
        for i in range(len(apartments_data_list) - 1):
            self.__wait_for_elem("input.whsOnd.zHQkBf")
            form_inputs = self.driver.find_elements(by=By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
            form_inputs[0].send_keys(apartments_data_list[i]["address"])
            form_inputs[1].send_keys(apartments_data_list[i]["price"])
            form_inputs[2].send_keys(apartments_data_list[i]["url"])
            time.sleep(1)
            submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.NqnGTe")
            submit_button.click()
            time.sleep(1)
            self.__goto_another_form()

    def create_spreadsheet(self):
        spreadsheet_button = self.driver.find_element(by=By.CSS_SELECTOR, value="div.uArJ5e.Y5FYJe.cjq2Db.M9Bg4d")
        spreadsheet_button.click()

    def quit_chrome(self):
        self.driver.quit()
