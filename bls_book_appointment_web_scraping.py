from log import Log
from requester import Requester
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time

class BLSBookAppWebScraping:

    def __init__(self, driver) -> None:
        self.driver = driver

    def set_birthday_picker(self, birthday) -> None:
        if self.set_picker_year(birthday.year):
            if self.set_picker_month(birthday.month):
                if not self.set_picker_day(birthday.day):
                    Log.e("Birth day not found")
            else:
                Log.e("Birth month not found")
        else:
            Log.e("Birth year not found")

    def set_passport_issue_date_picker(self, passport_issue_date) -> None:
        if self.set_picker_year(passport_issue_date.year):
            if self.set_picker_month(passport_issue_date.month):
                if not self.set_picker_day(passport_issue_date.day):
                    Log.e("Passport issue day not found")
            else:
                Log.e("Passport issue month not found")
        else:
            Log.e("Passport issue year not found")

    def set_passport_expiration_date_picker(self, passport_expiration_date) -> None:
        if self.set_picker_year(passport_expiration_date.year):
            if self.set_picker_month(passport_expiration_date.month):
                if not self.set_picker_day(passport_expiration_date.day):
                    Log.e("Passport expiration day not found")
            else:
                Log.e("Passport expiration month not found")
        else:
            Log.e("Passport expiration year not found")

    def set_picker_year(self, year):
        date_picker_years = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-years')))
        start_year = int(date_picker_years.find_element(By.XPATH, '/html/body/div[7]/div[3]/table/tbody/tr/td/span[1]').text)
        end_year = int(date_picker_years.find_element(By.XPATH, '/html/body/div[7]/div[3]/table/tbody/tr/td/span[12]').text)
        if start_year <= year <= end_year:
            for year_item in date_picker_years.find_elements(By.TAG_NAME, 'span'):
                if year == int(year_item.text):
                    year_item.click()
                    return True
            return False
        elif year < start_year:
            date_picker_years.find_element(By.CLASS_NAME, 'prev').click()
            return self.set_picker_year(year)
        elif year > end_year:
            date_picker_years.find_element(By.CLASS_NAME, 'next').click()
            return self.set_picker_year(year)
        else:
            return False
                
    def set_picker_month(self, month) -> bool:
        date_picker_months = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-months')))
        month_items = date_picker_months.find_elements(By.TAG_NAME, 'span')
        if 1 <= month <= len(month_items):
            month_items[month - 1].click()
            return True
        else:
            return False
        
    def set_picker_day(self, day) -> bool:
        date_picker_days = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-days')))
        day_items = date_picker_days.find_elements(By.XPATH, './/td[@class="day"]')
        for day_item in day_items:
            if int(day_item.text) == day:
                day_item.click()
                return True
        return False

    def current_time_in_sec(self) -> int:
        return round(time.time())

    def save_page_source(self, passport_number) -> None:
        timestamp = str(self.current_time_in_sec())
        html_file_name = 'html_page_'+passport_number+'_'+timestamp+'.html'
        path_to_save_html = '/Users/bryanarmijos/Projects/Python/BLSSpainVisaWebScraping/'+html_file_name
        Log.i(f"Printing html file = {html_file_name}")
        with open(path_to_save_html, "w", encoding='utf-8') as file:
            file.write(self.driver.page_source)

    def take_screenshot(self, passport_number) -> None:
        timestamp = str(self.current_time_in_sec())
        screenshot_file_name = passport_number+'_'+timestamp+'.png'
        path_to_save_screenshot = '/Users/bryanarmijos/Projects/Python/BLSSpainVisaWebScraping/'+screenshot_file_name
        Log.i(f"Taking screenshot = {screenshot_file_name}")
        self.driver.save_screenshot(path_to_save_screenshot)

    def fill_first_name(self, first_name) -> bool:
        try:
            input_first_name = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'first_name')))
            input_first_name.send_keys(first_name)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill first name input, Exception = {type(e)}")
            return False
        
    def fill_last_name(self, last_name) -> bool:
        try:
            input_last_name = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'last_name')))
            input_last_name.send_keys(last_name)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill last name input, Exception = {type(e)}")
            return False
        
    def fill_birthday(self, birthday) -> bool:
        try:
            input_date_of_birth = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'dateOfBirth')))
            input_date_of_birth.send_keys()
            self.set_birthday_picker(birthday)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill date of birth input, Exception = {type(e)}")
            return False
        
    def fill_passport_no(self, passport_number) -> bool:
        try:
            input_passport_number = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'passport_no')))
            input_passport_number.send_keys(passport_number)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill passport number input, Exception = {type(e)}")
            return False
        
    def fill_passport_issue_date(self, passport_issue_date) -> bool:
        try:
            input_ppt_issue_date = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'pptIssueDate')))
            input_ppt_issue_date.send_keys()
            self.set_passport_issue_date_picker(passport_issue_date)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill passport issue date input, Exception = {type(e)}")
            return False

    def fill_passport_expiration_date(self, passport_expiration_date) -> bool:
        try:
            input_ppt_expiry_date = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'pptExpiryDate')))
            input_ppt_expiry_date.send_keys()
            self.set_passport_expiration_date_picker(passport_expiration_date)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill passport expiration date input, Exception = {type(e)}")
            return False
        
    def fill_app_date(self, appointment_day: int = 0) -> bool:
        try:
            input_app_date_date = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'app_date')))
            input_app_date_date.send_keys()
            self.set_app_date_picker(appointment_day)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill app date input, Exception = {type(e)}")
            return False
        
    def set_app_date_picker(self, day: int) -> None:
        date_picker_days = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-days')))
        slots_available = WebDriverWait(date_picker_days, 300).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'activeClass')))
        slot_to_book = None
        # look for a slot with a given valid day
        if day > 0:
            for slot in slots_available:
                slot_value = slot.get_attribute('value')
                slot_day: int = int(slot_value) if slot_value is not None else 0
                if slot_day == day:
                    slot_to_book = slot
                    break
        # Set a default slot for booking if none is valid
        if slot_to_book is None:
            slots_available_size = len(slots_available)
            slot_to_book = slots_available[slots_available_size // 2]
        slot_to_book.click()

    def get_select_app_time(self, hour: str = '') -> bool:
        try:
            select_app_time = Select(WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, 'app_time'))))
            option_index: int = -1
            if hour != '':
                for index, option in enumerate(select_app_time.options):
                    Log.i(f"Option index = {index}")
                    option_value = option.get_attribute('value')
                    Log.i(f"Option value = {option_value}")
                    option_index = index if option_value is not None and option_value == hour else -1
                    if option_index is not -1: break
            else:
                option_size: int = len(select_app_time.options)
                Log.d(f"app time options size = {option_size}")
                option_index: int = int(option_size - (option_size / 3))
                Log.d(f"option_index = {option_index}")
            
            Log.d(f"the option_index is {option_index} and its value is {select_app_time.options[option_index].get_attribute('value')}")
            select_app_time.select_by_index(option_index)
            return True
        except Exception as e:
            Log.e(f"Exception on try to get select app time element, Exception = {type(e)}")
            return False
        
    def fill_passport_issue_place(self, passport_issue_place) -> bool:
        try:
            input_ppt_issue_place = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, 'pptIssuePalace')))
            input_ppt_issue_place.send_keys(passport_issue_place)
            return True
        except Exception as e:
            Log.e(f"Exception on try to fill passport issue place, Exception = {type(e)}")
            return False
        
    def get_select_visa_type_id(self) -> bool:
        try:
            select_visa_type = Select(WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'VisaTypeId'))))
            app_date_timeout = 300 # sec
            for i in range(1, app_date_timeout):
                selected_visa_type_text = select_visa_type.first_selected_option.text
                if selected_visa_type_text != "Seleccionar":
                    break
                else:
                    time.sleep(1)
            return True
        except Exception as e:
            Log.e(f"Exception on try to get select type visa element, Exception = {type(e)}")
            return False

    def check_captcha(self) -> None:
        captcha_timeout = 300 # sec
        for i in range(1, captcha_timeout):
            attr_value = self.driver.find_element(By.ID, 'captcha').get_attribute('value')
            captcha_text: str = ''
            if type(attr_value) == str: captcha_text = attr_value
            is_captcha_valid = len(captcha_text) >= 4
            if is_captcha_valid:
                break
            else:
                time.sleep(1)

    def wait_until_url_changes(self, current_url) -> None:
        WebDriverWait(self.driver, 60).until(EC.url_changes(current_url))

    def handle_alert(self) -> bool:
        try:
            WebDriverWait(self.driver, 60).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except Exception as e:
            Log.e(f"Exception on try to handle alert, Exception = {type(e)}")
            return False
        
    def call_book_appointment_endpoint(self, day, hour, requester: Requester):
        captcha: str = input('Ingresa el captcha')
        data = {
            'app_date': day,
            'loc_selected': 28,
            'mission_selected': 28,
            'VisaTypeld': 167,
            'first_nanme': requester.first_name,
            'last_name': requester.last_name,
            'dateOfBirth': requester.birthday.strftime('%Y-%m-%d'),
            'phone_code': 593,
            'phone': requester.phone,
            'nationalityld': 63,
            'passportType': '01',
            'passport_no': requester.passport_number,
            'pptissueDate': requester.passport_issue_date.strftime('%Y-%m-%d'),
            'pptExpiryDate': requester.passport_expiration_date.strftime('%Y-%m-%d'),
            'pptissuePalace': requester.passport_issue_place,
            'vasNos12': '',
            'vasNos1': '',
            'VasNos5': '',
            'VasNos6': '',
            'captcha': captcha,
            'save': 'Submit',
            'app_date_hidden': day,
            'type_hidden': '',
            'loc_final': 28,
            'countryID': 63,
            'missionId': 28,
        }
        pass
    
    def scrape_book_appointment_page(self, requester: Requester) -> None:
        day: str = '2024-04-24'
        hour: str = '08:45 - 09:00'

        self.fill_app_date()
        self.get_select_app_time(hour)
        self.get_select_visa_type_id()
        self.fill_first_name(requester.first_name)
        self.fill_last_name(requester.last_name)
        self.fill_birthday(requester.birthday)
        self.fill_passport_no(requester.passport_number)
        self.fill_passport_issue_date(requester.passport_issue_date)
        self.fill_passport_expiration_date(requester.passport_expiration_date)
        self.fill_passport_issue_place(requester.passport_issue_place)
        try:
            self.check_captcha()
            self.handle_alert()
            self.wait_until_url_changes(self.driver.current_url)
            self.driver.maximize_window()
            self.take_screenshot(requester.passport_number)
        except Exception as e:
            Log.e(f"Exception type = {type(e)}")
            Log.e(f"\n\n\n {e} \n\n\n")
        finally:
            free_time = 1800
            Log.d(f"Waiting {free_time / 60} minutes until quit the browser")
            time.sleep(free_time) # sec