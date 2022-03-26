import time
import config
import random

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

def time_format(string, time):
    print(f'{string}: {int((time)/60)} minutes and {(time)%60} seconds')

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
    time.sleep(config.vs_delay)
    # webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()

def change_resolution(driver):
    # DN2 ENT UP1 ENT ESC
    click_settings(driver)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ARROW_UP).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()
    time.sleep(config.vs_delay)

def change_speed(driver):
    click_settings(driver)

    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    time.sleep(config.vs_delay)

    webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()
    time.sleep(config.vs_delay)

def seek_video(driver):
    num_times = random.randint(config.min_, config.max_)
    time_format('Seeking', num_times * 5)
    while (num_times > 0):
        # print(num_times)
        webdriver.ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
        time.sleep(config.vs_delay)
        num_times -= 1

def main():
    while True:
        driver = initialize()

        # click_settings(driver)

        seek_video(driver)

        change_resolution(driver)

        change_speed(driver)

        # watch time can be made dynamic using randint
        time_format('Playback Time', config.watch_time)
        time.sleep(config.watch_time)

        driver.quit()

main()