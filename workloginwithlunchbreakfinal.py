from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml

with open('C:/Users/rmits/Desktop/work_login/config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    username = data['username']
    password = data['password']

options = webdriver.EdgeOptions()

options.add_experimental_option('detach', True) #stops browser from closing indefinitely
driver=webdriver.Edge(options=options)


#driver = webdriver.Edge('C:\Program Files (x86)\msedgedriver.exe')
time.sleep(5)
driver.get('https://secure.timesheets.com')



usrname = driver.find_element(By.NAME,'username')
time.sleep(2)
usrname.send_keys(username)

passwd = driver.find_element(By.NAME,'password')
passwd.send_keys(password)
time.sleep(5) #sleep to bypass popup

nextButton= driver.find_element(By.ID,'large-button-login')
nextButton.click()



time.sleep(5)
secondButton = driver.find_element(By.ID,'large-button-clockout')
secondButton.click()


time.sleep(30) #30 min lunch break

#clock back in after lunch


secondButton = driver.find_element(By.ID,'large-button-clockin')
secondButton.click()



driver.quit() #close page





