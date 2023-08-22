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

def browser_init() -> webdriver:
    service = Service(executable_path='chromedriver.exe')
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Edge(options=options)
    return browser

def data_parse():
    browser = browser_init()
    browser.get('https://m.dewu.com/router/')
    #SEARCHING FOR "SEARCH" ON PAGE
    data_parse = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view')))
    time.sleep(30) #ANTI-BAN
    data_parse.click()
    #SEARCHING INPUT ON SEARCH PAGE
    data = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view/uni-view[1]/uni-view/uni-input/div/form/input')))
    #TYPING ITEM`S NAME
    ActionChains(browser).send_keys_to_element(data, "Ni").perform()
    time.sleep(2)#ANTI-BAN
    ActionChains(browser).send_keys_to_element(data, "ke").perform()
    time.sleep(1)#ANTI-BAN
    ActionChains(browser).send_keys_to_element(data, " ").perform()
    time.sleep(1.3)#ANTI-BAN
    ActionChains(browser).send_keys_to_element(data, "D").perform()
    time.sleep(0.9)#ANTI-BAN
    ActionChains(browser).send_keys_to_element(data, "unk").perform()
    time.sleep(10)#ANTI-BAN   
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(30)#ANTI-BAN
    #RETURNING HTML
    data_parse = WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.XPATH, '/html')))
    time.sleep(60)#ANTI-BAN
    html_data = data_parse.get_attribute('innerHTML')
    print(html_data)

if __name__ == '__main__':
    data_parse()