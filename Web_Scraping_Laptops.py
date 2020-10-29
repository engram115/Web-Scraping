import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



if getattr(sys, 'Frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver.exe')
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome()

PATH = "chromedriver.exe"
url = 'https://www.lenovo.com/'
wp_url = "https://tech.ezgolearning.com/wp-login.php"
wp_uname = "info@tech.ezgolearning.com"
wp_pass = "o@y)LP2zm2Nz^&Fa8*"

#************************ WORD PRESS FUNCTION *****************************

def wordPress(title, images, description):
    driver.get(wp_url)
    search1 = driver.find_element_by_id("user_login")
    search1.clear()
    search1.send_keys(wp_uname)
    search1 = driver.find_element_by_id("user_pass")
    search1.clear()
    search1.send_keys(wp_pass)
    search1 = driver.find_element_by_id("wp-submit")
    search1.send_keys(Keys.RETURN)
    #driver.implicitly_wait(10)
    search1 = driver.find_element_by_link_text("New")
    search1.click()
    search1 = driver.find_element_by_id("title")
    search1.send_keys(title)

    compare0 = 0
    while(compare0 < len(images)):

        search1 = driver.find_element_by_id("insert-media-button")
        search1.send_keys(Keys.RETURN)
        # search1 = driver.find_element_by_link_text("Menu")
        # search1.click()
        search1 = driver.find_element_by_id("menu-item-embed")
        search1.click()
        search1 = driver.find_element_by_id("embed-url-field")
        search1.clear()
        image99 = images[compare0]
        search1.send_keys(image99)
        #search1.send_keys("<br>")
        time.sleep(1)
        search2 = driver.find_element(By.XPATH, '//button[text()="Insert into post"]')
        search2.send_keys(Keys.RETURN)
        time.sleep(3)
        #search2.click()
        compare0+=1

    search1 = driver.find_element_by_id("content_ifr")
    search1.send_keys(Keys.RETURN)
    compare = 0
    while(compare < len(description)):     # Upload Description of the Laptop

        out = "\n" + "* " + description[compare] + " : " + description[compare+1]
        if compare == len(description):
            search1.send_keys(compare)
            break
        else:
            search1.send_keys(out)
        compare+=2

    search1 = driver.find_element_by_id("publish")
    search1.send_keys(Keys.RETURN)

#************************ WORD PRESS FUNCTION END *****************************

driver = webdriver.Chrome(PATH)
driver.get(url)
print(driver.title)

search = driver.find_element_by_id("inputSearchText")
user_in = input("Enter Keyword (e.g. core i7, core i5, core i3): ")
search.send_keys(user_in)
search.send_keys(Keys.RETURN)
time.sleep(5)
list_of_hrefs = []

content_blocks = driver.find_elements_by_xpath("//a[@class='a-link learnMoreBtn product_adobeTagging -']") #Laptop Links

for block in content_blocks:             # All Laptop links saved in the List
    list_of_hrefs.append(block.get_attribute("href"))

for u in range(0, len(list_of_hrefs)):            # Delete Duplicate Links of Laptops
    for u1 in range(u+1, len(list_of_hrefs)-1):
        if list_of_hrefs[u] == list_of_hrefs[u1]:
            del list_of_hrefs[u1]

count = 0
while(count < len(list_of_hrefs)):
    driver.get(list_of_hrefs[count])
    laptop_name = driver.find_element_by_xpath("//h1[@class='desktopHeader']")  #  Laptop Model Name
    model_name = laptop_name.text

    search = driver.find_element_by_id("tab-techspec")
    data1=[]
    for table in driver.find_elements_by_xpath('//table[contains(@class,"techSpecs-table")]//tr'):   # Technical Specifications
        data = [item.text for item in table.find_elements_by_xpath(".//*[self::td]")]
        for d in data:
            data1.append(d)

    images = driver.find_elements_by_xpath("//div[@class='slick-slide']/img") # Images ofLaptop Model

    images_list = []
    for image in images:
        images_list.append(image.get_attribute("src"))

    wordPress(model_name, images_list, data1)               ####### Function Call
    count+=1

time.sleep(5)
driver.close()


