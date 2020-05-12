from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
import threading

event = threading.Event()


def play_video(song):
    # Set up the driver for firfox and find the youtube video from selenium
    fp = webdriver.FirefoxProfile(r'C:\Users\juanr\AppData\Roaming\Mozilla\Firefox\Profiles\josdp49b.default-release-1583268249046')
    #fp.add_extension(extension='adblock_plus-3.8-an fx.xpi')
    driver = webdriver.Firefox(
        executable_path=r'C:\Users\juanr\Desktop\Nudes\geckodriver-v0.26.0-win64\geckodriver.exe',
        firefox_profile= fp)



    driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located
    driver.get("https://www.youtube.com/results?search_query=" + song)
    
    # play the video
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()

    # Gets the video duration then sleeps for the duration of the
    time.sleep(1)
    duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]

    # checks the time duration of a youtube video
    duration_text = duration.text
    current_video_time = str_to_secs(duration_text)

    # Deals with 2 ads sometimes...
    if current_video_time < 60:
        time.sleep(current_video_time)

        # write this better
        time.sleep(1)
        duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
        time.sleep(1)
        duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
        duration_text = duration.text
        current_video_time = str_to_secs(duration_text)
        if current_video_time < 60:
            time.sleep(1)
            duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]
            time.sleep(1)
            duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]

        duration_text = duration.text
        current_video_time = str_to_secs(duration_text)
        print('Ad Over')

    print(current_video_time)
    event.wait(current_video_time)
    driver.quit()

    #kill_firefox_window()



# Parses through string of text from IRC server and searches Youtube
def youtube_command(self,e):
    try:
        search_words = e.arguments[0].split()
        search_words.pop(0)
        search_words_str = ''
        for word in search_words:
            search_words_str += f'{word} '
        self.video_queue.put(search_words_str)

    except TypeError:
        print('No arguments passed')


# 'HH:MM:SS' => total secs , turns string of time to secs
def str_to_secs(time_string):
    try:
        time_split = [int(i) for i in time_string.split(':')]
        if len(time_split) == 3:
            total_time = time_split[0] * 3600 + time_split[1] * 60 + time_split[2]
        if len(time_split) == 2:
            total_time = time_split[0] * 60 + time_split[1]
        if len(time_split) == 1:
            total_time = time_split[0]
    except:
        total_time = 30

    return total_time


def playing_video_loop(video_queue):
    while True:
        event.clear()
        url_string = video_queue.get()
        play_video(url_string)
