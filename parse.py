from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
import pandas as pd
import time
from bs4 import BeautifulSoup
import cv2
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path='chromedriver.exe')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome\chrome.exe"
# chrome_options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(service=service, options=chrome_options)
# browser.get('https://m.dewu.com/router/')

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)
browser.get('https://m.dewu.com/router/')

# page = WebDriverWait(browser, 25).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view'))
# )
# time.sleep(3)
# page.click()

# data = WebDriverWait(browser, 25).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view/uni-view[1]/uni-view/uni-input/div/form/input')))

# ActionChains(browser).send_keys_to_element(data, "Nike Dunk").perform()
# time.sleep(3)   
# ActionChains(browser).send_keys(Keys.ENTER).perform()
# time.sleep(30)


data_parse = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view')))
time.sleep(30)
data_parse.click()

data = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view/uni-view[1]/uni-view/uni-input/div/form/input')))

ActionChains(browser).send_keys_to_element(data, "Ni").perform()
time.sleep(2)
ActionChains(browser).send_keys_to_element(data, "ke").perform()
time.sleep(1)
ActionChains(browser).send_keys_to_element(data, " ").perform()
time.sleep(1.3)
ActionChains(browser).send_keys_to_element(data, "D").perform()
time.sleep(0.9)
ActionChains(browser).send_keys_to_element(data, "unk").perform()


time.sleep(10)   
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(30)

data_parse = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.XPATH, '/html')))


time.sleep(60)

html_data = data_parse.get_attribute('innerHTML')
print(html_data)


# for i in range(0, 1459):
#     try:




#         img = cv2.imread('')

#     except:
#         print(f'error ({i})')

