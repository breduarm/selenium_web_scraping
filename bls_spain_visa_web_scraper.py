from bls_login_web_scraping import BLSLoginWebScraping
from bls_agree_terms_web_scraping import BLSAgreeTermsWebScraping
from bls_book_appointment_web_scraping import BLSBookAppWebScraping
from log import Log
from requester import Requester
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import constants

class BLSSpainVisaWebScraper:

    def __init__(self, requester: Requester) -> None:
        self.url_bls_login = constants.URL_BLS_LOGIN_GUAYAQUIL
        self.url_bls_appointment = constants.URL_BLS_APPOINTMENT_GUAYAQUIL
        self.requester: Requester = requester
        if self.requester.is_from_quito():
            self.url_bls_login = constants.URL_BLS_LOGIN_QUITO
            self.url_bls_appointment = constants.URL_BLS_APPOINTMENT_QUITO

        service = Service(executable_path=constants.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

    def scrape(self) -> None:
        Log.i(f"Scraping with requester data = {self.requester.first_name} {self.requester.last_name} \n", True)

        self.driver.get(self.url_bls_login)
            
        # Login Page
        login_page = BLSLoginWebScraping(self.driver)
        login_page.scrape_login_page(self.requester)

        # Agree Terms Page
        agree_terms_page = BLSAgreeTermsWebScraping(self.driver)
        agree_terms_page.scrape_agree_terms_page(self.url_bls_appointment)

        # Book Appointment Page
        book_appointment = BLSBookAppWebScraping(self.driver)
        book_appointment.scrape_book_appointment_page(self.requester)

        self.driver.quit()