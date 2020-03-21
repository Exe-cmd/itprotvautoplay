## This script auto plays CEH v10 Certified ethical hacker v10 videos in ITPROTV in the web browser

import requests
import webbrowser
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

UserName='' ###ITPROTV USERNAME###
PassWord='' ###ITPROTV PASSWORD###
url='https://app.itpro.tv/course-library/ceh-v10/overview-cehv10/?autostart=1'
video=1
#videoTime=[540,1334,1740,1200,1680]

#Install Chome Driver and open itpro.tv in chrome
#Install chromedriver https://chromedriver.chromium.org/downloads
#save to rename path to where your chromedriver is located
driver = webdriver.Chrome(executable_path='/home/executables/Desktop/chromedriver')
driver.get(url)

driver.find_element_by_name('username').send_keys(UserName)
driver.find_element_by_name('password').send_keys(PassWord)
driver.find_element_by_id('loginform').click()
loginbutton = driver.find_element_by_xpath("//*[@id='loginform']/button")
loginbutton.click()

time.sleep(10) ###allow time for page to load
while video < 100:

    playvid = driver.find_element_by_id("jwPlayerVideo")
    playvid.click()

    #Sleeps for however long the video goes 
    #time.sleep(videoTime[video])    
    time.sleep(1500) ###25minutes in seconds placeholder until all video times are in the array

    playvid = driver.find_element_by_id("episode-next-episode")
    playvid.click()
    video+1
