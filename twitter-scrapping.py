from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

#Maximizing browser window to avoid hidden elements
driver.set_window_size(1024, 600)
driver.maximize_window()

## Opening website
driver.get('https://twitter.com/GuildOfGuardian/followers%27)
           
## waiting load
time.sleep(2)
follower_list = []
nick_list = []
           
# Code to goto End of the Page
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    for i in range(1,100):
        try:
            follower = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span')
            nick = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/a/div/div[2]/div/span')
            soup_follower = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')
            soup_nick = BeautifulSoup(nick.get_attribute('outerHTML'), 'html.parser')
            if soup_follower not in follower_list:
                follower_list.append(soup_follower.text)
            if soup_nick not in follower_list:
                nick_list.append(soup_nick.text)
        except NoSuchElementException:
            pass
           
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
           
    # Wait to load page
    time.sleep(1)
           
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
len(follower_list)
df = pd.DataFrame(list(zip(follower_list, nick_list)), columns =['UserName', '@'])

df.to_csv('twitter_followers.csv', sep=';')

