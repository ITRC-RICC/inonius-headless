#!/usr/bin/env python3
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    print('Access to inonius.net')
    driver.get('https://inonius.net/')
    time.sleep(2)
    
    print('Start to measure')
    button = driver.find_element_by_id('startTestBtn')
    button.click()

    print('Wait 40 seconds for the result...')
    time.sleep(40)

    w = driver.execute_script('return document.body.scrollWidth;')
    h = driver.execute_script('return document.body.scrollHeight;')
    driver.set_window_size(w,h)
    driver.save_screenshot('result.png')
    print('The result was saved as result.png')
except:
    traceback.print_exc()
finally:
    driver.quit()

