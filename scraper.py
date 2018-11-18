from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/p/BqUfulwH6O4/')
time.sleep(3)

load_more_comment = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button')
i = 0
try:
    while load_more_comment.is_displayed() and i < 25:
        load_more_comment.click()
        i += 1
        time.sleep(3)
except:
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