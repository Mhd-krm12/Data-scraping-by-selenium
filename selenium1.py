# go to github.com 

import time
from selenium import webdriver

driver=webdriver.Chrome()               #kullanılan browser
url = "https://github.com/"             #istenilen site url'i
driver.get(url)

time.sleep(2)
print(driver.title)
driver.maximize_window()                #büyük ekran
driver.save_screenshot("S1.png")       #ekran alıntısı alma

url="https://github.com/python"
driver.get(url)
print(driver.title)

if "Python" in driver.title:
    driver.save_screenshot("S2.png")

print(driver.title)
time.sleep(2)

driver.back()
time.sleep(2)
driver.close()


time.sleep(2)
print(driver.close())
