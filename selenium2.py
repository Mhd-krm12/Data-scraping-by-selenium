import time
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()                                   #chrome browther kullan
url="https://github.com/"                                    
driver.get(url)                                             # url deki siteye git
time.sleep(2)



searchInput=driver.find_element_by_name("q")                # isminden elementi bul
time.sleep(2)                                               # 1 saniye bekle

searchInput.send_keys("python")                             # ""içindki kelemeyi yaz (element içine)
time.sleep(2)


searchInput.send_keys(Keys.ENTER)                           # enter tuşune tıkla
time.sleep(2)

#result=driver.page_source
result = driver.find_element_by_css_selector(" #js-pjax-container > div > header > div.container-xl.pt-4.pt-lg-0.p-responsive.clearfix > div > div:nth-child(1)")   # css selector ile elementi bul
for element in result:                                                 
    print(element.text)


driver.close()
