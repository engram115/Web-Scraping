import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# if getattr(sys, 'Frozen', False):
#     chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver.exe')
#     driver = webdriver.Chrome(chromedriver_path)
# else:
#     driver = webdriver.Chrome()

PATH = "chromedriver.exe"
url = 'https://www.macys.com/'

driver = webdriver.Chrome(PATH)
driver.get(url)

search = driver.find_element_by_css_selector("map")
print(search.text)
#content_blocks = driver.find_elements_by_xpath('//*[contains(@area)]')

time.sleep(5)
# list_of_hrefs = []
#
# content_blocks = driver.find_elements_by_xpath("//a[@class='a-link learnMoreBtn product_adobeTagging -']") #Laptop Links
#
# for block in content_blocks:             # All Laptop links saved in the List
#     list_of_hrefs.append(block.get_attribute("href"))
#
# for u in range(0, len(list_of_hrefs)):            # Delete Duplicate Links of Laptops
#     for u1 in range(u+1, len(list_of_hrefs)-1):
#         if list_of_hrefs[u] == list_of_hrefs[u1]:
#             del list_of_hrefs[u1]
#
# count = 0
# while(count < len(list_of_hrefs)):
#     driver.get(list_of_hrefs[count])
#     laptop_name = driver.find_element_by_xpath("//h1[@class='desktopHeader']")  #  Laptop Model Name
#     model_name = laptop_name.text
#
#     search = driver.find_element_by_id("tab-techspec")
#     data1=[]
#     for table in driver.find_elements_by_xpath('//table[contains(@class,"techSpecs-table")]//tr'):   # Technical Specifications
#         data = [item.text for item in table.find_elements_by_xpath(".//*[self::td]")]
#         for d in data:
#             data1.append(d)
#
#     images = driver.find_elements_by_xpath("//div[@class='slick-slide']/img") # Images ofLaptop Model
#
#     images_list = []
#     for image in images:
#         images_list.append(image.get_attribute("src"))
#
#     wordPress(model_name, images_list, data1)               ####### Function Call
#     count+=1

time.sleep(5)
driver.close()


