import getpass
import string

from selenium import webdriver
import time
import sys


def isRedirectedToLoginPage(driver) -> bool:
    try:
        username_field = driver.find_element_by_name('username')
        password_field = driver.find_element_by_name('password')
        return username_field is not None and password_field is not None
    except:
        return False


def getUsername() -> string:
    username = input("Username: ")
    return username


def getPassword() -> string:
    password = getpass.getpass("Password: ")
    return password


def login(driver, username: string, password: string):
    username_field = driver.find_element_by_name('username')
    username_field.sendKeys(username)

    password_field = driver.find_element_by_name('password')
    password_field.sendKeys(password)

    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()


def askLoginCredential(driver):
    username = getUsername()
    password = getPassword()
    print("username: ", username, "password: ", password, end="\n")
    login(driver, username, password)


driver = webdriver.Chrome()
driver.get(sys.argv[1])
time.sleep(3)

# if user not logged in
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass

if isRedirectedToLoginPage(driver):
    askLoginCredential(driver)

try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(sys.argv[2]):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)

import excel_exporter

excel_exporter.export(user_names, user_comments)

driver.close()
