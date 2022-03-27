import time
import config
import random
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

video_has_chapters = False # whether the video has chapters

def current_time(text):
    print(f'{text} [{datetime.now().strftime("%H:%M:%S")}]')

def time_format(string, time):
    print(f'{string}: {int((time)/60)} minutes and {(time)%60} seconds')

# initializes and returns web-driver
def initialize():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(config.driver_file, options=options)
    driver.get(config.link)
    
    current_time('Bot Started')
    
    time.sleep(config.long_delay) # to ensure page load
    return driver

# clicks the settings button on playback window (to get the context menu)
def click_settings(driver):
    global video_has_chapters
    try:
        settings = driver.find_element(By.XPATH, config.settings_btn)
    except:
        settings = driver.find_element(By.XPATH, config.settings_btn_2)
        video_has_chapters = True
    
    settings.click()
    time.sleep(config.vs_delay)
    # webdriver.ActionChains(driver).key_down(Keys.ESCAPE).perform()

# changes video resolution to 144p
def change_resolution(driver):
    # DN2 ENT UP1 ENT ESC
    click_settings(driver)

    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)
    
    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(config.vs_delay)
    
    # additional keypress if chapters are present
    global video_has_chapters
    if video_has_chapters:
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

    print('Changed Resolution to 144p')

# changes video speed to 2x
def change_speed(driver):
    click_settings(driver)

    # additional keypress
    global video_has_chapters
    if video_has_chapters:
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(config.vs_delay)

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

    print('Changed Speed to 2x')

# seeks further into the video
def seek_video(driver):
    num_times = random.randint(config.min_, config.max_)
    time_format('Seeking', num_times * 5)
    while (num_times > 0):
        # print(num_times)
        webdriver.ActionChains(driver).key_down(Keys.ARROW_RIGHT).perform()
        time.sleep(config.vs_delay)
        num_times -= 1

# main loop
def main():
    watched = 1
    while True:
        driver = initialize()

        seek_video(driver)

        change_resolution(driver)

        change_speed(driver)

        # time_format('Playback Time', config.watch_time) # displays info in console
        # time.sleep(config.watch_time)

        # or use this for randomized watch time
        watch_time = random.randint(config.min_wt, config.max_wt)
        time_format('Playback Time', watch_time)
        time.sleep(watch_time)
        
        print(f'Watched {watched} times')

        watched += 1

        driver.quit()

        current_time('Loop Ended')
        print('---')        

main()