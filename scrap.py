import numpy as np
from selenium import webdriver

### Selenium' library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





from time import sleep




class ScrapBk:

    def __init__(self, url_home:str) -> None:
        
        self.url_home = url_home
        
        
        
        
        
        pass

    def create_webdriver(self) -> webdriver:
        ### Options para ChromeDriver
         self.options   = Options()
         self.options.add_argument("--start-maximized")
         self.prefs = {"profile.default_content_setting_values.geolocation" :2}
         self.options.add_experimental_option("prefs",self.prefs)

         self.driver = webdriver.Chrome(options=self.options)
         self.driver.get(self.url_home)

         return self.driver
        
    def click_xpath(self, x_path_target:str, current_driver:webdriver) -> None:
        
        element = current_driver.find_element(By.XPATH, x_path_target)
        element.click()
        sleep(1)

        return None




