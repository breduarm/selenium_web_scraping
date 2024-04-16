from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import time
import re

# Web site and browser data

# web = 'https://ecuador.blsspainvisa.com/guayaquil/book_appointment.php'
web = 'https://ecuador.blsspainvisa.com/quito/book_appointment.php'
path = '/Users/bryanarmijos/Projects/Python/chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)

###############################################################





###############################################################

# Login data

phone = "985466277"
email = "scbwcz93@duck.com"

# Personal data

name = "JANETH GABRIELA"
last_name = "GUANIN YANCHAPAXI"
birthday_str = "1989-12-22"
birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()

# Passport data

passport_number = "A9668543"
passport_issue_date_str = "2023-05-30"
passport_issue_date = datetime.strptime(passport_issue_date_str, '%Y-%m-%d').date()
passport_expiration_date_str = "2033-05-30"
passport_expiration_date = datetime.strptime(passport_expiration_date_str, '%Y-%m-%d').date()
passport_issue_place = "QUITO"

###############################################################

# # Login data

# phone = "998533534"
# email = "7xnvhqsf@duck.com"

# # Personal data

# name = "JOSE EDMUNDO"
# last_name = "ESCOBAR RECALDE"
# birthday_str = "1958-11-14"
# birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()

# # Passport data

# passport_number = "A9239829"
# passport_issue_date_str = "2024-01-29"
# passport_issue_date = datetime.strptime(passport_issue_date_str, '%Y-%m-%d').date()
# passport_expiration_date_str = "2034-01-29"
# passport_expiration_date = datetime.strptime(passport_expiration_date_str, '%Y-%m-%d').date()
# passport_issue_place = "QUITO"

###############################################################

# # Login data

# phone = "939421270"
# email = "xfqb5udf@duck.com"

# # Personal data

# name = "DAVID ALEJANDRO"
# last_name = "TUTACHA REYES"
# birthday_str = "2009-10-05"
# birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()

# # Passport data

# passport_number = "A8739631"
# passport_issue_date_str = "2023-04-18"
# passport_issue_date = datetime.strptime(passport_issue_date_str, '%Y-%m-%d').date()
# passport_expiration_date_str = "2033-04-18"
# passport_expiration_date = datetime.strptime(passport_expiration_date_str, '%Y-%m-%d').date()
# passport_issue_place = "QUITO"

###############################################################





###############################################################

# Auto form filling

select_center = Select(driver.find_element(By.ID, 'centre'))
select_center.select_by_index(1)
time.sleep(5) # TODO nor work
select_category = Select(driver.find_element(By.ID, 'category'))
select_category.select_by_index(1)
driver.find_element(By.ID, 'phone').send_keys(phone)
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'verification_code').click()
otp_code = driver.find_element(By.ID, 'otp')

# TODO check otp code message error  "Google captcha verification failed."

otp_timeout = 60 # sec
for i in range(1, otp_timeout):
    otp_code_text = otp_code.get_attribute('value')
    is_otp_valid = len(otp_code_text) == 4
    if is_otp_valid:
        break
    else:
        time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="em_tr"]/div[3]/input').click()

# Second page Agree Terms

agree_button = driver.find_element(By.XPATH, '//*[@id="EcuadarSecond"]/section/div/div/div/div[3]/div[1]/button')
driver.execute_script('arguments[0].click();', agree_button)

def set_app_date_picker():
    date_picker_days = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-days')))
    day_items = date_picker_days.find_elements(By.TAG_NAME, 'td')
    groups = {}
    for day_item in day_items:
        title = day_item.get_attribute('title')
        if title in groups:
            groups[title].append(day_item)
        else:
            groups[title] = [day_item]
    slots_available = groups['Slots Full']
    slots_available_size = len(slots_available)
    slots_available[slots_available_size // 2].click()

def set_birthday_picker():
    if set_picker_year(birthday.year):
        if set_picker_month(birthday.month):
            if not set_picker_day(birthday.day):
                print("\n ==== Birth day not found ERROR ==== \n")
        else:
            print("\n ==== Birth month not found ERROR ==== \n")
    else:
        print("\n ==== Birth year not found ERROR ==== \n")

def set_passport_issue_date_picker():
    if set_picker_year(passport_issue_date.year):
        if set_picker_month(passport_issue_date.month):
            if not set_picker_day(passport_issue_date.day):
                print("\n ==== Passport issue day not found ERROR ==== \n")
        else:
            print("\n ==== Passport issue month not found ERROR ==== \n")
    else:
        print("\n ==== Passport issue year not found ERROR ==== \n")

def set_passport_expiration_date_picker():
    if set_picker_year(passport_expiration_date.year):
        if set_picker_month(passport_expiration_date.month):
            if not set_picker_day(passport_expiration_date.day):
                print("\n ==== Passport expiration day not found ERROR ==== \n")
        else:
            print("\n ==== Passport expiration month not found ERROR ==== \n")
    else:
        print("\n ==== Passport expiration year not found ERROR ==== \n")

def set_picker_year(year):
    date_picker_years = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-years')))
    start_year = int(date_picker_years.find_element(By.XPATH, '/html/body/div[7]/div[3]/table/tbody/tr/td/span[1]').text)
    end_year = int(date_picker_years.find_element(By.XPATH, '/html/body/div[7]/div[3]/table/tbody/tr/td/span[12]').text)
    print(f"\n ==== year_from = {start_year} | year_to = {end_year} | year = {year}")
    if start_year <= year <= end_year:
        for year_item in date_picker_years.find_elements(By.TAG_NAME, 'span'):
            if year == int(year_item.text):
                year_item.click()
                return True
        return False
    elif year < start_year:
        date_picker_years.find_element(By.CLASS_NAME, 'prev').click()
        return set_picker_year(year)
    elif year > end_year:
        date_picker_years.find_element(By.CLASS_NAME, 'next').click()
        return set_picker_year(year)
    else:
        return False
            
def set_picker_month(month):
    date_picker_months = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-months')))
    month_items = date_picker_months.find_elements(By.TAG_NAME, 'span')
    if 1 <= month <= len(month_items):
        print(f"\n ==== month selected = {month_items[month - 1].text}")
        month_items[month - 1].click()
        return True
    else:
        return False
    
def set_picker_day(day):
    date_picker_days = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-days')))
    day_items = date_picker_days.find_elements(By.XPATH, './/td[@class="day"]')
    for day_item in day_items:
        if int(day_item.text) == day:
            print(f"\n ==== day selected = {day_item.text}")
            day_item.click()
            return True
    return False

def current_time_in_sec():
    return round(time.time())

def save_page_source():
    timestamp = str(current_time_in_sec())
    html_file_name = 'html_page_'+passport_number+'_'+timestamp+'.html'
    path_to_save_html = '/Users/bryanarmijos/Projects/Python/BLSSpainVisaWebScraping/'+html_file_name
    print(f"\n ==== Printing html file = {html_file_name}")
    with open(path_to_save_html, "w", encoding='utf-8') as file:
        file.write(driver.page_source)

def take_screenshot():
    timestamp = str(current_time_in_sec())
    screenshot_file_name = passport_number+'_'+timestamp+'.png'
    path_to_save_screenshot = '/Users/bryanarmijos/Projects/Python/BLSSpainVisaWebScraping/'+screenshot_file_name
    print(f"\n ==== Taking screenshot = {screenshot_file_name}")
    driver.save_screenshot(path_to_save_screenshot)





################################################################################

flag = False
if flag:
    driver.find_element(By.ID, 'app_date').send_keys()
    set_app_date_picker()

    # TODO replace de ID value with the appointment time one.
    select_app_time = Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'loc_selected'))))
    select_app_time.select_by_index(8)

    time.sleep(1)
    select_visa_type = Select(driver.find_element(By.ID, 'VisaTypeId'))
    select_visa_type.select_by_index(1)
else:
    driver.find_element(By.ID, 'app_date').send_keys()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'datepicker-days')))
    save_page_source()

    # TODO duplicated from line 55. This is temporary we should not use this.
    app_date_timeout = 180 # sec
    select_visa_type = Select(driver.find_element(By.ID, 'VisaTypeId'))
    for i in range(1, app_date_timeout):
        selected_visa_type_text = select_visa_type.first_selected_option.text
        if selected_visa_type_text != "Seleccionar":
            break
        else:
            time.sleep(1)

##################################################################################





save_page_source()

driver.find_element(By.ID, 'app_date').send_keys(Keys.ENTER)

driver.find_element(By.ID, 'first_name').send_keys(name)
driver.find_element(By.ID, 'last_name').send_keys(last_name)

driver.find_element(By.ID, 'dateOfBirth').send_keys()
set_birthday_picker()

driver.find_element(By.ID, 'passport_no').send_keys(passport_number)

driver.find_element(By.ID, 'pptIssueDate').send_keys()
set_passport_issue_date_picker()

driver.find_element(By.ID, 'pptExpiryDate').send_keys()
set_passport_expiration_date_picker()

driver.find_element(By.ID, 'pptIssuePalace').send_keys(passport_issue_place)

captcha_timeout = 120 # sec
for i in range(1, captcha_timeout):
    captcha_text = driver.find_element(By.ID, 'captcha').get_attribute('value')
    is_captcha_valid = len(captcha_text) >= 4
    if is_otp_valid:
        break
    else:
        time.sleep(1)

current_url = driver.current_url
WebDriverWait(driver, 60).until(EC.url_changes(current_url))

driver.maximize_window()
take_screenshot()

time.sleep(5)

driver.quit()