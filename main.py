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
    time.sleep(config.long_delay) # to ensure page load
    return driver

def click_settings(driver):
    settings = driver.find_element(By.XPATH, config.settings_btn)
    settings.click()
    time.sleep(config.short_delay)
    webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()

def change_resolution(driver):
    pass

def change_speed(driver):
    pass

def seek_video(driver):
    num_times = random.randint(config.min_, config.max_)
    print(f'Video seeking for {int((num_times * 5)/60)} minutes and {(num_times * 5)%60} seconds')
    while (num_times > 0):
        # print(num_times)
        webdriver.ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
        time.sleep(config.vs_delay)
        num_times -= 1

def main():
    while True:
        driver = initialize()

        click_settings(driver)

        seek_video(driver)

        # watch time
        print(f'Video will play for {int((config.watch_time)/60)} minutes and {(config.watch_time)%60} seconds')
        time.sleep(watch_time)

        driver.quit()

main()