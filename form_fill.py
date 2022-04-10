from selenium import webdriver
from selenium.webdriver.chrome.service import Service

FORM_URL = r"https://docs.google.com/forms/d/e/1FAIpQLSensmGNGsalUpAS8whkm8ESlOCKgwbIOa-RPA5y_iX8UM6UOw/viewform?usp=sf_link"
CHROME_DRIVER_PATH = r"C:\Users\Kowalczyk\PycharmProjects\chromedriver.exe"


class FormFill:

    def __init__(self):
        chrome_service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(FORM_URL)
