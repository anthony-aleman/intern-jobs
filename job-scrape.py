from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os
import time

# load environment variables
load_dotenv()
INTERN = 'Software Engineer Intern'
WHERE=os.getenv('HOME')

# configure the driver to use Chrome
driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver')
driver.implicitly_wait(3)

# list to store job postiton titles
positions = []

# list to store the company names
company_name = []

# list to store job location
location = []

# navigate to link
driver.get('https://www.indeed.com/')



# job entry
driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys(INTERN)


# location entry
#driver.find_element_by_xpath('//*[@id="text-input-where"]')


# search
# sometimes one xpath works and sometimes the other xpath works
try:
    driver.find_element_by_xpath('//*[@id="jobsearch"]/button').click()
except Exception:
    print(f'recieved exception: {Exception}')

try:
    driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()
except Exception:
    print(f'recieved exception: {Exception}')


# store the page content
#content = driver.page_source
#soup = BeautifulSoup(content, features='html.parser')


# finding all the job posting elements
job_postings = driver.find_elements_by_class_name('job_seen_beacon')

for job_card in job_postings:
    print(job_card.text)
    # TODO: scrape the name, location, salary and reviews if there are any