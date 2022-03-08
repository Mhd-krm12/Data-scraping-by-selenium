from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Twitter:
    def __init__(self):

        # Browser and language
        self.browserProfile = webdriver.ChromeOptions()                                                   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})    
        self.browserProfile.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome( options = self.browserProfile)                              

    
    def fonk(self):            
        self.browser.get("https://twitter.com/firatresmihesap")  
        self.browser.maximize_window()
                                          
        time.sleep(10)
        results=[]

        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            # Wait to load page
            time.sleep(5)


            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")

            # break condition
            if last_height == new_height :
                break
            last_height = new_height

            tweets = self.browser.find_elements(by=By.CLASS_NAME, value='css-901oao.r-1fmj7o5.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
            time.sleep(2)

            for i in tweets:
                results.append(i.text)

            count = 1
            with open("tweets.txt","w",encoding="UTF-8") as file:
                for item in results:
                    file.write(f"{count}-{item}\n")
                    count+=1        

            # textfile = open("a_file.txt", "w")
            # for element in results:
            #     textfile.write( element + "\n")
            
            
            # textfile.close()           



twitter=Twitter()
twitter.fonk()
