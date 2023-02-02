%load_ext autoreload
%autoreload 2 # Essas linhas atualiza o script/classe


import numpy as np

### Selenium' library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from time import sleep


from scrap import *


### BeautifulSoap
from bs4 import BeautifulSoup



sc = ScrapBk(url_home='https://order.burgerking.com.ar/')
sc.create_webdriver()
x_path_reject = '//*[@id="app"]/div/div[2]/div/div[2]/button[2]'

sc.click_xpath(x_path_reject, sc.driver)





click_xpath(x_path_reject, driver)


x_path_local = '//*[@id="app"]/div/div[1]/div/div[1]/div/div/div/button[1]'
click_xpath(x_path_local, driver)

x_path_ok = '//*[@id="confirmation"]/div/button'
click_xpath(x_path_ok, driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')
var = soup.find_all('h2', {'class': 'c-button__title'})

restaurant = [x.text.strip() for x in var]
restaurant





