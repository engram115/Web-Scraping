import os, sys, csv, os.path, time
from os import path
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
url = 'https://www.psx.com.pk/'
fname = "PSX.csv"

driver = webdriver.Chrome(PATH)
driver.get(url)
title = driver.title

def WriteData():
    localtime = time.asctime(time.localtime(time.time()))
    f.write("\n" + "Date & Time: " + localtime)
    f.write("\n" + hh)
    f.write(dd)

while True:

    search = driver.find_element_by_xpath("//div[@class='market-overview']/h2")
    a = search.text.split()
    a1 = a[0] + " " + a[1]


    head_list = []
    hh = ""
    heads = driver.find_elements_by_xpath("//div[contains(@class, 'market-overview')]//th")
    for head in heads:
        head_list.append(head.text)
    for h in range(0, len(head_list)):
        hh = hh + head_list[h] + ", "


    data_list = []
    dd = "\n"
    count=0
    dataz = driver.find_elements_by_xpath("//div[contains(@class, 'market-overview')]//td")
    for data in dataz:
        data_list.append(data.text.replace(",", ""))
    for d in range(0, len(data_list)):
        count1 = count + (len(head_list)-1)
        if d == count1:
            dd=dd + data_list[d] + "\n"
            count += len(head_list)
        else:
            dd = dd + data_list[d] + ", "

    fileExist=1
    if not path.exists(fname):
        fileExist=0

    f = open(fname, "a", encoding="utf-8")

    if fileExist==0:
        f.write(title)
        f.write("\n" + a1)
        WriteData()
    else:
        WriteData()

    time.sleep(20)
driver.close()