from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

times_to_loop = int(input('Times to loop?\n'))
delay = 30
driver = webdriver.Chrome()
driver.get("http://i.mooc.chaoxing.com")
while True:
    input('Enter any key to continue.')
    if '学习进度页面' in driver.title:
        break
    else:
        print('Open course page in your original tab.')

for elem in driver.find_elements_by_class_name('clearfix'):
    try:
        orange_status = elem.find_element_by_class_name('orange')
    except:
        pass
    else:
        course_link = elem.find_element_by_xpath(
            './/a[@href]').get_attribute('href')
        driver.get(course_link)
        break

for i in range(times_to_loop):
    try:
        driver.switch_to.default_content()
        iframe = driver.find_element_by_id('iframe')
        driver.switch_to.frame(iframe)
        driver.switch_to.frame(0)

        try:
            play_button = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'vjs-big-play-button')))
        except:
            print('Could not find play button.')
        else:
            print('Video found. Starting video.')
            play_button.click()

        while True:
            duration_tag = driver.find_element_by_class_name(
                'vjs-duration-display')
            if duration_tag.text != "0:00" and duration_tag.text:
                break
        print(f"Video duration is {duration_tag.text}")
        round_to_next_minute = int(duration_tag.text.split(':')[0]) + 1
        print(f'Sleeping for {round_to_next_minute} minutes.')
        time.sleep(round_to_next_minute * 60)

    except:
        print('No video found on this page. Proceeding to next page.')

    driver.switch_to.default_content()
    try:
        next_page = driver.find_element_by_id('right2')
    except:
        try:
            next_page = driver.find_element_by_id('right3')
        except:
            next_page = driver.find_element_by_class_name('orientationright')
    print('Clicking next page.')
    next_page.click()

    time.sleep(10)
