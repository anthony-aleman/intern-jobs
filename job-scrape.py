from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()
INTERN = 'Software Engineer Intern'
WHERE=os.getenv('HOME')

# configure the driver to use Chrome
driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver')


# list to store job postiton titles
positions = []

# list to store the company names
company_name = []

# list to store job location
location = []

# navigate to link
driver.get('https://www.indeed.com/')

# job entry
job = driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys(INTERN)
job.send_keys('\n')

# location entry
driver.find_element_by_xpath('//*[@id="text-input-where"]')

# search
search = driver.find_element_by_xpath('//*[@id="jobsearch"]/button')
search.click()

# store the page content
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')

for a in soup.find_all('a', attrs={'class': 'slider_container'}):
    print(a)