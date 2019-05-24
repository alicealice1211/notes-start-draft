"""
Created on Wed Apr  4 00:19:01 2018
illnois Cities
@author: alice
"""
import os
import time
import csv
import shutil
import random 
import urllib
import unittest
import pandas as pd
from datetime import datetime
from selenium import webdriver
from time import gmtime, strftime
from collections import OrderedDict
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#URL
#.current_url
def headLess():
    options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images':2}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--no-sandbox')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-default-apps')



#    options.add_argument('--proxy-server=%s' % PROXY)
#    options.add_argument("--headless");
#    options.add_argument("--disable-gpu")
    
    
   
    driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\alice\Desktop\chromedriver.exe')  
#    driver = webdriver.Chrome(r'C:\Users\Mom\Desktop\SoftwareStuff\Webdrivers\chromedriver')
    driver.get('https://www.dlapiper.com/en/us/people/')

def tab1():#Open a new tap 
    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    
    
def tab0():#switch back to old tap
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


#######################
search.send_keys(u'\ue003'*int(random.randint(210,300)))
#delete

search.send_keys(keyword+(u'\ue007'))
#enter key
driver.find_element_by_xpath('//input[@aaria-label="Password"]').click()

#firefox
driver = webdriver.Firefox(executable_path=r'C:\Users\alice\Desktop\Geckodriver\geckodriver.exe')
driver.get('https://app.chatra.io/')
global j
##########################


xpath
.find('..')
#all parents

def setUp():
    global driver
    driver = webdriver.Chrome(executable_path=r'C:\Users\alice\Desktop\chromedriver')
    driver.get('')

#driver.find_element_by_xpath('//div[@class="zsg-media-bd"]/h1').get_attribute("innerHTML")
def parse():
    try:
            =
        print(''+str())
        List.append()
    except:
        print(' : NA')
        List.append('NA')
def scrollDown1():#for followerTap
    body =driver.find_element_by_xpath('//body')
    body.send_keys(Keys.PAGE_DOWN)
    shortWait()
    body.send_keys(Keys.PAGE_DOWN)
    shortWait()
    body.send_keys(Keys.PAGE_DOWN)
    shortWait()
    body.send_keys(Keys.PAGE_DOWN)
    shortWait()
    body.send_keys(Keys.PAGE_DOWN)
    shortWait()
def goBack():
    driver.execute_script('window.history.go(-1)')

def longWait():
    time.sleep(random.randint(40,60))
    
def wait():
    time.sleep(random.randint(15,20)*0.235)
    
def shortWait():
    time.sleep(random.randint(8,10)*0.2102)
aList=[]
bList=[]
cList=[]
dList=[]
eList=[]
fList=[]
gList=[]
hList=[]
iList=[]
jList=[]
kList =[]  

df = pd.read_csv(r'C:\Users\alice\Downloads\ttto.csv')
df1 = df[0][1:]
df2 = df[1][1:]
df3 = df[2][1:]
df4 = df[3][1:]
df5 = df[4][1:]
df6 = df[5][1:]
df7 = df[6][1:]
df8 = df[7][1:]
df9 = df[8][1:]
df10 = df[9][1:]
df11 = df[10][1:]

def panda_to_pkl():
    df = pd.read_csv(r'C:\Users\alice\Downloads\ttto.csv')
    df.to_pickle('tttopickled_output.pkl')
    
    
def csv_from_excel():
    wb = xlrd.open_workbook(r'C:\Users\alice\Downloads\ttto.xlsx')
    sh = wb.sheet_by_index(0)

    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
def createList():
    for a in df1:
        aList.append(a) 
        
    for b in df2:
        bList.append(b)
    
    for c  in df3:
        cList.append(c)  
        
    for d in df4:
        dList.append(d)    
    
    for e in df5:
        eList.append(e)    
    
    for f in df6:
        fList.append(f)    
    
    for g in df7:
        gList.append(g) 
    
    for h in df8:
        hList.append(h)  
    for i in df9:
        iList.append(i)  
    for j in df10:
        jList.append(j)  
    for k in df11:
        kList.append(k)  

row0=["title","title","title","title","title","title","title","title","title","title","title"]
def save():       
    file_name = (input("file name:")+".csv")
#    rows=zip(zipList)
    rows=zip(aList,bList,cList,dList,eList,fList,gList,h8List,iList,jList)
 
    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        links_writer=csv.writer(csvfile)
        links_writer.writerow(row0)
        for item in rows:
            links_writer.writerow(item)
    print("csv file saved")   
    


# for i in x:
    driver.find_elements_by_xpath('//figcaption[@class="caption"]'+ str(i+1) + '/a')
#child element I think
    textBlocks=driver.find_elements_by_xpath('//figcaption[@class="caption"]/following::p[1]')
    
    
    
    
    
    
    
    
    


    for i in photoOrder:
    try:
#            img = driver.find_elements_by_xpath('//ul[@class="photos"]//img')
        img=driver.find_elements_by_xpath('//li[@class="sm-tile"]//img')
        src = img[i].get_attribute('src')#img URL
        miniWait()
        try:
            urllib.request.urlretrieve(src, str(fileName)+str(photoName)+"Number"+str(i)+".png")
            photoNameE.append(str(fileName)+str(photoName)+"Number"+str(i)+".png")
        except:
            print("skip one photo")

    
    
    
#####Scroll DOWN/UP
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_DOWN)
    
######using beautiful soup
def parsePage_using_beautiful_soup(url):
    global s
    r = requests.get(url, headers=RandomHeaders.LoadHeader())                     
    soup = bs4.BeautifulSoup(r.text, "lxml")   
    s=soup
    
    title(soup)                    
    buyNew(soup)                                                              
    
    ISBN(soup)
    

def varibale_using_above_soup_fucntion(soup): #not including shipping
    global price
    price='NA'
    try:
        prices= soup.find_all('span', {'class':'olp-padding-right'})                  
        for i in prices:                                                              
            if 'New from' in i.text:                                                 
                price=str(i.text).split('$')[1].strip()   
                                            
    except:
        price='NA'
    print('new price= '+str(price))                                      
    newPriceList.append(price)                       
######using beautiful soup
    


# remove file /delete file using shutil
    shutil.rmtree(path)
    
###########FTP
    
ftp.mkd('pathname')# create a new directory
ftp.cwd('//testing') #set the current directory
ftp.retrlines('LIST') #check everything ls
ftp.cwd('..')
ftp.getweclome()
ftp.storbinary('STOR'+str(fileName),open(filePath,'rb')) #send the file
open(filePath,'rb').close()
ftp.quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
