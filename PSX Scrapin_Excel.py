import os, sys, csv, os.path, time, xlsxwriter
from os import path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "chromedriver.exe"
url = 'https://www.psx.com.pk/'
fname = "PSX.xlsx"


driver = webdriver.Chrome(PATH)
driver.get(url)
title = driver.title
fileExist=1

r = 0; c = 0; r1 = 3
workbook = xlsxwriter.Workbook(fname)
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
italic = workbook.add_format({'italic': True})
center = workbook.add_format({'align': 'center'})
if not path.exists(fname):
    fileExist = 0
else:
    fileExist = 1
x = 1
while x<=3:

    search =  driver.find_element_by_xpath("//div[@class='market-overview']/h2")
    a = search.text.split()
    a1 = a[0] + " " + a[1]

    head_list = []
    hh = ""
    heads = driver.find_elements_by_xpath("//div[contains(@class, 'market-overview')]//th")
    for head in heads:
        head_list.append(head.text)

    data_list = []
    dataz = driver.find_elements_by_xpath("//div[contains(@class, 'market-overview')]//td")
    for data in dataz:
        data_list.append(data.text)

    if fileExist == 0:
        row = r
        col = c
        localtime = time.asctime(time.localtime(time.time()))
        worksheet.write(row, col, title)
        row+=1
        worksheet.write(row, col, a1)
        row+=2
        worksheet.write(row, col, localtime)
        row+=1
        for h in head_list:
            worksheet.write(row, col, h)
            col+=1
        row+=1
        col=0
        i=5
        for d in range(0, len(data_list)):
            worksheet.write(row, col, data_list[d])
            if d == i:
                worksheet.write(row, col, data_list[d])
                row += 1
                i += 6
                r1=row+2
                col = 0
            else:
                col+=1
        #workbook.close()
        fileExist=1
    else:
        row = r1
        col = c
        localtime = time.asctime(time.localtime(time.time()))
        worksheet.write(row, col, localtime)
        row+=1
        for h in head_list:
            worksheet.write(row, col, h)
            col+=1
        row+=1
        col=0
        i = 5
        for d in range(0, len(data_list)):
            worksheet.write(row, col, data_list[d])
            if d == i:
                worksheet.write(row, col, data_list[d])
                row += 1
                i += 6
                r1 = row+2
                col=0
            else:
                col+=1
        #workbook.close()

    c=0
    time.sleep(5)
    x+=1
workbook.close()
driver.close()
