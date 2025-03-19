from selenium import webdriver
import time
import sys
from selenium.webdriver.common.by import By

service = webdriver.FirefoxService(executable_path="/home/asdf/geckodriver")

driver = webdriver.Firefox(service=service)

url="https://www.instagram.com/"

driver.get(url) 

time.sleep (2)

"""
On the first project of me which we entered Twitter without using password,we use XPaths of
elements but in Instagram,when we refresh our website,id number of login url changes so we need
to use something different to use that link through Python Selenium. Either we can choose class name
or name selectors to use that.
"""
username=driver.find_element(By.NAME,"username")
username.send_keys ('USER-NAME')

password =driver.find_element (By.NAME,"password")
password.send_keys('PASSWORD')
password.submit()


time.sleep(10)



driver.get(sys.argv[1])

time.sleep(4)



# load "sys.argv[2]" comments 
try:
    load_more_comment = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/li/div/button')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(sys.argv[2]):
        load_more_comment.click()
        time.sleep(7)
        load_more_comment = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/li/div/button')
        print(i)
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass



user_names = []
user_comments = []
comment = driver.find_elements(By.CLASS_NAME,'_a9ym')
for c in comment:
    container = c.find_element(By.CLASS_NAME,'_a9zr')
    name = container.find_element(By.CLASS_NAME,'_a9zc').text
    content = container.find_element(By.TAG_NAME,'span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)
# print(user_names)
# print(user_comments)
import excel_exporter
excel_exporter.export(user_names, user_comments)

driver.close()
