from log import Log
from requester import Requester
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time

class BLSLoginWebScraping:

    def __init__(self, driver) -> None:
        self.driver = driver
    
    def get_select_center(self) -> bool:
        try:
            select_center = Select(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'centre'))))
            select_center.select_by_index(1)
            return True
        except Exception as e:
            Log.e(f"Exception on try to get center select element, Exception type = {type(e)}")
            return False
        
    def get_select_category(self) -> bool:
        try:
            select_category = Select(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'category'))))
            timeout = 60 # sec
            for i in range(1, timeout):
                category_options_size: int = len(select_category.options)
                if category_options_size > 1:
                    break
                else:
                    time.sleep(1)
            select_category.select_by_index(1)
            return True
        except Exception as e:
            Log.e(f"Exception on try to get category select element, Exception type = {type(e)}")
            return False
        
    def fill_phone(self, phone) -> bool:
        try:
            input_phone = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'phone')))
            input_phone.send_keys(phone)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill phone input, Exception type = {type(e)}")
            return False
        
    def fill_email(self, email) -> bool:
        try:
            input_email = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'email')))
            input_email.send_keys(email)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill email input, Exception type = {type(e)}")
            return False
        
    def click_verification_code(self) -> bool:
        try:
            submit_verification_code = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'verification_code')))
            self.driver.execute_script('arguments[0].click();', submit_verification_code)
            return True
        except Exception as e:
            Log.e(f"Exception on try to click verification code, Exception type = {type(e)}")
            return False
        
    def was_otp_code_sent(self) -> bool:
        try:
            captcha_failed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Captcha verification failed.")]')))
            return False if captcha_failed else True
        except Exception as e:
            Log.e(f"Exception on try to check if the otp code was sent successfully, Exception type = {type(e)}")
            return True

    def check_otp_code(self) -> bool:
        try:
            otp_code = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'otp')))
            timeout = 500 # sec
            is_otp_valid = False
            for _ in range(1, timeout):
                attr_value = otp_code.get_attribute('value')
                otp_code_text: str = ''
                if type(attr_value) == str : otp_code_text = attr_value
                is_otp_valid: bool = len(otp_code_text) == 4
                if is_otp_valid:
                    break
                else:
                    time.sleep(1)
            return is_otp_valid
        except Exception as e:
            Log.e(f"Exception on try to check the otp code, Exception type = {type(e)}")
            return False
        
    def submit_form(self) -> bool:
        try:
            is_otp_valid: bool = self.check_otp_code()
            if is_otp_valid :
                submit_form = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="em_tr"]/div[3]/input')))
                self.driver.execute_script('arguments[0].click();', submit_form)
            return is_otp_valid
        except Exception as e:
            Log.e(f"Exception on try to submit the form, Exception type = {type(e)}")
            return False
        
    def scrape_login_page_2(self, requester: Requester) -> None:
        self.get_select_center()
        self.get_select_category()
        self.fill_phone(requester.phone)
        self.fill_email(requester.email)
        self.click_verification_code()
        was_otp_code_sent: bool = self.was_otp_code_sent()
        if was_otp_code_sent:
            self.submit_form()
        else:
            self.click_verification_code()
            self.submit_form()

    def scrape_login_page(self, requester: Requester) -> None:
        self.get_select_center()
        self.get_select_category()
        self.fill_phone(requester.phone)
        self.fill_email(requester.email)
        time.sleep(2)
        self.submit_form()