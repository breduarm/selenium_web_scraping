from log import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BLSAgreeTermsWebScraping:

    def __init__(self, driver) -> None:
        self.driver = driver

    def click_agree_terms(self) -> bool:
        try:
            agree_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="EcuadarSecond"]/section/div/div/div/div[3]/div[1]/button')))
            self.driver.execute_script('arguments[0].click();', agree_button)
            return True
        except Exception as e:
            Log.e(f"Exception on try to click agree terms button, Exception = {type(e)}")
            return False

    def wait_until_url_contains(self, url) -> None:
        WebDriverWait(self.driver, 120).until(EC.url_contains(url))

    def scrape_agree_terms_page(self, url) -> None:
        self.click_agree_terms()
        self.wait_until_url_contains(url)