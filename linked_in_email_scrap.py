# If An error is raised,,,,  then Increase the "sleep time" as the internet speed may be slower enough....


# Importing Important Modules

from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
import requests

#  creating the instance of web driver & Sending the url  request

driver = webdriver.Chrome(executable_path='C:\\Users\Khushi Raj\Desktop\driver\chromedriver')
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('rr82354305@gmail.com')
time.sleep(2)
driver.find_element_by_id('password').send_keys('13/06/91')
driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button").click()
driver.find_element_by_xpath("//*[@id='mynetwork-nav-item']/a").click()  # click on Mynetwork link to find All new Friend's
time.sleep(5)

#  Find the "Total Connectoins in List" & then  click to iterate through each connections
frnd_size = int(driver.find_element_by_xpath("/html/body/div[6]/div[5]/div[4]/div/div/div/div/div/aside/div[1]/section/div/div[1]/a/div/div[2]").text)
time.sleep(5)
con_clk = driver.find_element_by_xpath("/html/body/div[6]/div[5]/div[4]/div/div/div/div/div/aside/div[1]/section/div/div[1]/a").click()
time.sleep(5)

## Use For loop to iterate through all "Connections" .....
for req in range(frnd_size):
    driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[3]/div/div/div/div/div/div/div/div/section/ul/li[" + str(req+1) + "]/div/div[1]/a").click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[3]/a').click()
    time.sleep(5)
    page_soup = soup(driver.page_source, 'lxml')
    time.sleep(10)
    container = page_soup.find('div', attrs={'class': 'pv-profile-section__section-info section-info'})
    email_container = container.find('section', attrs={'class': 'pv-contact-info__contact-type ci-email'})
    email = email_container.find('div', attrs={'class': 'pv-contact-info__ci-container'}).find('a').text.strip()
    url = 'www.' + container.find('section', attrs={'class': 'pv-contact-info__contact-type ci-vanity-url'}).find('a').text.strip()
    Name = page_soup.find('h1', attrs={'id': 'pv-contact-info'}).text.strip()
    print(Name + ' : ' + email, + " : " + url)
    driver.back()
    driver.back()
driver.close()

