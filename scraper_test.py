from selenium import webdriver
import time
import sys
from selenium.webdriver.common.by import By
import re
import pandas as pd

driver = webdriver.Chrome()

url="https://www.instagram.com/"

driver.get(url) 

time.sleep (2)

"""
On the first project of me which we entered Twitter without using password,we use XPaths of
names but in Instagram,when we refresh our website,id number of login url changes so we need
to use something different to use that link through Python Selenium. Either we can choose class name
or name selectors to use that.
"""
username=driver.find_element(By.NAME,"username")
username.send_keys ('6361118782')

password =driver.find_element (By.NAME,"password")
password.send_keys('insta!!@@##12')
password.submit()


time.sleep(10)



driver.get(sys.argv[1])

time.sleep(4)

user_names = []
user_comments = []
user_comment_containers = []
user_profile_links = []

def update_csv():
    # Create a DataFrame from the lists
    df = pd.DataFrame({'User Names': user_names, 'User Comments': user_comments,'User Comment Containers': user_comment_containers,'User Profile Links': user_profile_links})

    # Write DataFrame to CSV file
    df.to_csv('data.csv', index=False)



def extract_comment(text):
    # Define the pattern to match the comment
    pattern = re.compile(r'\b\d+[dmhyw]\b\n(.*?)\n\d+\s+(likes|like)', re.DOTALL)

    # Find the comment using the pattern
    match = re.search(pattern, text)

    # Extract and return the comment message
    if match:
        return match.group(1)
    else:
        return None


def set_user_and_comment():
    time.sleep(1)
    global start_comment_index, end_comment_index
    for i in range(start_comment_index, end_comment_index+1):
        comment_container = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div['+str(i)+']')
        name = comment_container.find_element(By.CLASS_NAME, '_ap3a').text
        print(f'comments context:({i}){comment_container.text}\n\n')
        comment = extract_comment(comment_container.text)
        profile_link = "https://www.instagram.com/"+name
        user_names.append(name)
        user_comments.append(comment)
        user_comment_containers.append(comment_container.text)
        user_profile_links.append(profile_link)
        update_csv()



# load "sys.argv[2]" comments
try:
    global start_comment_index, end_comment_index
    element = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]')

    comments_container = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]')
    names = comments_container.find_elements(By.CLASS_NAME, '_ap3a')
    print(f'no of elements before scrolling:{len(names)}')
    start_comment_index = 1
    end_comment_index = len(names)
    temp = 0

    time.sleep(2)

    while(temp<int(sys.argv[2])):
        set_user_and_comment()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
        time.sleep (2)
        start_comment_index=end_comment_index+1
        names = comments_container.find_elements(By.CLASS_NAME, '_ap3a')
        end_comment_index = len(names)
        temp = temp+1
        time.sleep(1)
    set_user_and_comment()

    


    print(f'user name:{user_names} len:{len(user_names)}\n\nuser comments:{user_comments} len:{len(user_comments)}')




    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
    # time.sleep (2)
    # names = comments_container.find_elements(By.CLASS_NAME, '_ap3a')
    # print(f'no of elements after first scrolling:{len(names)}')
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
    # time.sleep (2)
    # names = comments_container.find_elements(By.CLASS_NAME, '_ap3a')
    # print(f'no of elements after second scrolling:{len(names)}')

    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
    # time.sleep (2)
    # names = comments_container.find_elements(By.CLASS_NAME, '_ap3a')
    # print(f'no of elements after third scrolling:{len(names)}')


    # names = element.find_elements(By.CLASS_NAME, '_ap3a')

    # for name in names:
    #     print(name.text)

    

except Exception as e:
    print(e)
    pass

# driver.close()

    # element = driver.find_element(By.XPATH,'//div[@data-visualcompletion]')

    # print(element.text)
    # driver.execute_script("arguments[0].scrollIntoView();", element)