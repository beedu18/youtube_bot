import time
import config
import random

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

def initialize():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("start-maximized")

    driver = webdriver.Chrome("./chromedriver.exe", options=options)
    driver.get(config.link)
    return driver

def click_settings(driver):
    settings = driver.find_element(By.XPATH, config.settings_btn)
    settings.click()
    webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()

def seek_video(driver):
    num_times = random.randint(config.min_, config.max_)
    print(f'Video seeking for {num_times} taps')
    while (num_times > 0):
        # print(num_times)
        webdriver.ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
        time.sleep(config.vs_delay)
        num_times -= 1

def main():
    driver = initialize()
    time.sleep(config.long_delay) # to ensure page load
    
    click_settings(driver)
    time.sleep(config.short_delay)

    seek_video(driver)
    time.sleep(config.long_delay)
    
    driver.quit()

main()