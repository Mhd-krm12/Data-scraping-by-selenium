
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username=input("Telefon numarası, e-posta veya kullanıcı adı giriniz:   ") 
password=input("şifreyi giriniz:   ")
class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def singIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(4)

        usernameInput = self.browser.find_element_by_name("text")
        usernameInput.send_keys(self.username)

        searchInput=self.browser.find_element_by_name("text")       
        searchInput.send_keys(Keys.ENTER)                           
        time.sleep(4)

        password = self.browser.find_element_by_name("password")
        password.send_keys(self.password)
        time.sleep(4)

        searchInput=self.browser.find_element_by_name("password")   
        searchInput.send_keys(Keys.ENTER)                           
        time.sleep(4)
twitter = Twitter(username,password)
twitter.singIn()        

