from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException 

# check existance by xpath
def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# check existance by css selector
def check_exists_by_css_selector(driver,css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True

# open browser
driver = webdriver.Chrome('/home/gopal/Desktop/scrapper/chromedriver')
driver.get("https://www.wincher.com/")

# login to account
found=False
while(found==False):
    found=check_exists_by_xpath(driver,'//*[@id="navigation"]/div/a[5]')    
print("Login Button")

button=driver.find_element_by_xpath('//*[@id="navigation"]/div/a[5]')
button.click()
username='info@montaigne.co'
password='montaigne@123'

found=False
while(found==False):
    found=check_exists_by_xpath(driver,'//*[@id="userName"]')    
print("Username Password")

driver.find_element_by_xpath('//*[@id="userName"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.execute_script('document.getElementsByClassName("w-btn btn-orange")[0].click()')

# to open competitor page 
found=False
while(found==False):
    found=check_exists_by_css_selector(driver,'#top > div.wrapper > div > article > div > div > div > div > div:nth-child(8) > div > ul > li:nth-child(3) > a') 
print("Competitor Button")
driver.execute_script("document.querySelectorAll('#top > div.wrapper > div > article > div > div > div > div > div:nth-child(8) > div > ul > li:nth-child(3) > a')[0].click()")
count=0
# move to the next pages till last
for i in range(13):   
    # to check table is loaded successfully
    found=False
    while(found==False):
        found=check_exists_by_css_selector(driver,'#top > div.wrapper > div > article > div > div > div > div > div:nth-child(2) > div.table-responsive > table')        
    print('Table Loaded')    

    # to check button is loaded successfully
    found=False
    while(found==False):
        found=check_exists_by_css_selector(driver,'#top > div.wrapper > div > article > div > div > div > div > div:nth-child(8) > div > ul > li:nth-child(3) > a')         
    print("Next Button Loaded") 
    driver.execute_script('document.querySelectorAll("#top > div.wrapper > div > article > div > div > div > div > div:nth-child(2) > div.pull-left.pagination.ng-isolate-scope > ul > li:nth-child(8) > a")[0].click()')
    print("Next Button Clicked and Current Page No: ",(i+2))

    
    

# # extracting table data
# print("{ looking for table data }")
# found=False
# while(found==False):
#     found=check_exists_by_css_selector(driver,'#top > div.wrapper > div > article > div > div > div > div > div:nth-child(2) > div.table-responsive > table') 
# print("table element found")
# table=driver.find_element_by_css_selector('#top > div.wrapper > div > article > div > div > div > div > div:nth-child(2) > div.table-responsive > table')
# print(table.text)

# #putting table data into a file
# with open('table_text.txt', '+a') as the_file:
#     the_file.write(table.text)

       

