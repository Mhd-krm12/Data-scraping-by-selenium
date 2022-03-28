from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import xlsxwriter


class Twitter:
    def __init__(self):

        
        self.browserProfile = webdriver.ChromeOptions()                                                   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})    
        self.browserProfile.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome( options = self.browserProfile)                              

    
    def fonk(self):            
        self.browser.get("https://twitter.com/firatresmihesap")                                            
        time.sleep(10)
        

        results=[]
        #scroll
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        
        new_height = 0
        while True:
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(10)
            print(str(new_height) + "--------" + str(last_height))          
            if last_height == new_height:
                break
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")

            last_height = new_height
            tweets = self.browser.find_elements(by=By.CLASS_NAME, value='css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
            
            for i in tweets:
                results.append(i.text)

            textfile = open("a_file.txt", "w")
            for element in results:
                textfile.write(element + "\n")
            textfile.close()           



twitter=Twitter()
twitter.fonk()
