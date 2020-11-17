#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import requests, bs4
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import pandas as pd
import smtplib


#Enter the URL of site where you will extract the price data from
url1 = 'https://flight.easemytrip.com/FlightList/Index?org=IXR-Ranchi,%20India&dept=DEL-Delhi,%20India&adt=1&chd=0&inf=0&cabin=0&airline=undefined&deptDT=30/11/2019&arrDT=undefined&isOneway=true&isDomestic=true&&lang='
url2 = "https://flight.easemytrip.com/FlightList/Index?org=IXR-Ranchi,%20India&dept=DEL-Delhi,%20India&adt=1&chd=0&inf=0&cabin=0&airline=Any&deptDT=28/11/2019&arrDT=&isOneway=true&isDomestic=true&CouponCode=&lang="
url3 = "https://flight.easemytrip.com/FlightList/Index?org=IXR-Ranchi,%20India&dept=DEL-Delhi,%20India&adt=1&chd=0&inf=0&cabin=0&airline=Any&deptDT=29/11/2019&arrDT=&isOneway=true&isDomestic=true&CouponCode=&lang="
url4 = "https://flight.easemytrip.com/FlightList/Index?org=IXR-Ranchi,%20India&dept=DEL-Delhi,%20India&adt=1&chd=0&inf=0&cabin=0&airline=undefined&deptDT=01/12/2019&arrDT=undefined&isOneway=true&isDomestic=true&&lang="


#Function to Check the price
def check_price():

    driver = webdriver.Firefox()


    driver.get(url1)
    time.sleep(10)
    fare30 = driver.find_elements_by_xpath("//*[@class = 'col-md-8 col-sm-8 col-xs-9 txt-r6-n ng-binding']")
    for text in fare30:
        a.append(int(text.text.replace(',','')))

    driver.get(url2)
    time.sleep(10)
    fare28 = driver.find_elements_by_xpath("//*[@class = 'col-md-8 col-sm-8 col-xs-9 txt-r6-n ng-binding']")
    for text in fare28:
        b.append(int(text.text.replace(',','')))
    

    driver.get(url3)
    time.sleep(10)
    fare29 = driver.find_elements_by_xpath("//*[@class = 'col-md-8 col-sm-8 col-xs-9 txt-r6-n ng-binding']")

    for text in fare29:
        c.append(int(text.text.replace(',','')))

    driver.get(url4)
    time.sleep(10)
    fare1 = driver.find_elements_by_xpath("//*[@class = 'col-md-8 col-sm-8 col-xs-9 txt-r6-n ng-binding']")
    for text in fare1:
        d.append(int(text.text.replace(',','')))
    
    driver.get('https://www.happyeasygo.com/flights/IXR-DEL/2019-11-30?tripType=0&adults=1&childs=0&baby=0&cabinClass=Economy&airline=&carrier=')
    time.sleep(10)
    fare30_HEG = driver.find_elements_by_xpath("//*[@class = 'o-name price-origin test']")

    for text in fare30_HEG:
        a_HEG.append(int(text.text.replace(',','').replace('₹', '').strip()))

    driver.get('https://www.happyeasygo.com/flights/IXR-DEL/2019-11-28?tripType=0&adults=1&childs=0&baby=0&cabinClass=Economy&airline=&carrier=')   
    time.sleep(10)
    fare28_HEG = driver.find_elements_by_xpath("//*[@class = 'o-name price-origin test']")

    for text in fare28_HEG:
        b_HEG.append(int(text.text.replace(',','').replace('₹', '').strip()))


    driver.get('https://www.happyeasygo.com/flights/IXR-DEL/2019-11-29?tripType=0&adults=1&childs=0&baby=0&cabinClass=Economy&airline=&carrier=')   
    time.sleep(10)
    fare29_HEG = driver.find_elements_by_xpath("//*[@class = 'o-name price-origin test']")

    for text in fare29_HEG:
        c_HEG.append(int(text.text.replace(',','').replace('₹', '').strip()))

    driver.get('https://www.happyeasygo.com/flights/IXR-DEL/2019-12-01?tripType=0&adults=1&childs=0&baby=0&cabinClass=Economy&airline=&carrier=')   
    time.sleep(10)
    fare1_HEG = driver.find_elements_by_xpath("//*[@class = 'o-name price-origin test']")

    for text in fare1_HEG:
        d_HEG.append(int(text.text.replace(',','').replace('₹', '').strip()))


    driver.close()
    print(a,'\n\n', b, '\n\n', c , '\n\n',d, '\n\n', a_HEG, '\n\n', b_HEG, '\n\n', c_HEG,'\n\n', d_HEG )
    
    for i in range(0,3):
    
        if len(a) != 0 and len(a) > 2 and a[i] < 5000 : send_mail("30" + str(i))
        
        if len(b) != 0 and len(b) > 2 and b[i] < 5000 :  send_mail('28' + str(i))
        
        if len(c) != 0 and len(c) > 2 and c[i] < 5000 : send_mail('29' + str(i))
    
        if len(d) != 0 and len(d) > 2 and d[i] < 5000 : send_mail('1' + str(i))
        
        if len(a_HEG) != 0 and len(a_HEG) > 2 and a_HEG[i] < 5000 : send_mail('30HEG' + str(i))
        
        if len(b_HEG) != 0 and len(b_HEG) > 2 and b_HEG[i] < 5000 : send_mail('28HEG' + str(i))
        
        if len(c_HEG) != 0 and len(c_HEG) > 2 and c_HEG[i] < 5000 : send_mail('29HEG' + str(i))
        
        if len(d_HEG) != 0 and len(d_HEG) > 2 and d_HEG[i] < 5000: send_mail('1HEG' + str(i))


#Function to send mail
def send_mail(ip):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('your id','your token')
    
    subject = 'price for' + ip + 'fell down'
    body = 'Check HEG or EMT as per the Subject'
    
    msg = f"Subject : {subject}\n\n{body}"
    server.sendmail('from address', 'to address',msg)
    print("Hey Email has been sent!!")
    
    server.quit()

    
while True:
    a = []
    b = []
    c = []
    d=[]
    a_HEG = []
    b_HEG = []
    c_HEG = []
    d_HEG=[]

    check_price()
    time.sleep(900)


    


# In[ ]:




