#!/usr/bin/env python
# coding: utf-8

# In[1]:


## importing libraries
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


## Open browser
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
#Maximizing browser window to avoid hidden elements
driver.set_window_size(1024, 600)
driver.maximize_window()


# In[3]:


## Opening linkedin website
driver.get('https://twitter.com/GuildOfGuardian')
## waiting load
time.sleep(2)


# In[11]:


#driver.find_element_by_class_name('css-1dbjc4n').click()
#css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0
follower = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span')                                       
html(/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span)
html(/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span)


# In[198]:


follower_list = []


# In[19]:


soup = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')


# In[20]:


follower_list.append(soup.text)


# In[195]:


follower_list = []


# In[159]:


last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(1,60000):
    follower = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span')                                       
    soup = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')
    follower_list.append(soup.text)
    # Code to goto End of the Page
    for user in range (1, len(jobs)+1):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
usernames = driver.find_element_by_class_name("css-1dbjc4n")
user_count = usernames.find_elements_by_class_name('css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')


# In[199]:


last_height = driver.execute_script("return document.body.scrollHeight")
user_count = 1
count = 1
# Code to goto End of the Page
while True:
    usernames = driver.find_element_by_class_name("css-1dbjc4n")
    user_count = usernames.find_elements_by_class_name('css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')
    for user in range(count, len(user_count)+1):
        follower = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{user}]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span')                                       
        soup = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')
        follower_list.append(soup.text)
       
    count = len(user_count)+1
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
        #follower = driver.find_elements_by_class_name('css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
       
   


# In[122]:


# Code to goto End of the Page
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# In[160]:


follower_list


# In[161]:


len(follower_list)


# In[185]:


usernames = driver.find_element_by_class_name("css-1dbjc4n")
user_count = usernames.find_elements_by_class_name('css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')#here we select each job to count
print(len(user_count))


# In[191]:


#usernames = driver.find_element_by_class_name("css-1dbjc4n")
#user_count = usernames.find_elements_by_class_name('css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')
#follower = driver.find_elements_by_class_name('css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
soup = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')
#follower_list.append(soup.text)


# In[196]:


last_height = driver.execute_script("return document.body.scrollHeight")
user_count = 1
count = 1
# Code to goto End of the Page

usernames = driver.find_element_by_class_name("css-1dbjc4n")
user_count = usernames.find_elements_by_class_name('css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg')
for user in range(count, len(user_count)+1):
    follower = driver.find_element_by_xpath(f'/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/section/div/div/div[{user}]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span')                                       
    soup = BeautifulSoup(follower.get_attribute('outerHTML'), 'html.parser')
    follower_list.append(soup.text)
       
jobs_lists = driver.find_element_by_class_name('jobs-search-results__list') #here we create a list with jobs
    jobs = jobs_lists.find_elements_by_class_name('jobs-search-results__list-item')#here we select each job to count


# In[216]:


usernames = driver.find_elements_by_class_name("css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
for username in usernames:
        username = usernames.find_element_by_class_name("css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
        print(username)
        


# In[203]:


len(usernames)


# In[220]:


import http
import requests


# In[223]:




url = 'https://api.twitter.com/1.1/followers/list.json?user_id=GuildOfGuardian&count=200'



resp = requests.get(url=url)
data = resp.json() 


# In[224]:


data

