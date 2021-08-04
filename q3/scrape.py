from connection import *
from check import *
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import fb_cred

import time
# def err(username):
#     print(f"Username {username} is not valid")

def dec(function):
    def wrapper(username):
        my_cursor = conn.cursor()
        query = "SELECT * FROM user where username= '{}'".format(username)
        my_cursor.execute(query)
        table_data = my_cursor.fetchall()
        if len(table_data) != 0:
            for item in table_data:
                # print(res)
                if username in item:
                    done = user_check(table_data)
                    # print(done)
                    if (done is None):
                        function(username)
                    else:
                        user_check(table_data).show()
        else:
            raise ValueError('User not valid')


    return wrapper

@dec
def scrap(username):
    url = "https://m.facebook.com/{}/about".format(username)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())


    name = soup.find('h3')
    name = name.string
    print(name)


    for i in soup.find_all('div'):
        if i.string == "कार्य":
            break
    i = i.parent.parent.parent.parent.parent.contents[1]
    work = []
    for div in i.children:
        work.append(div.contents[0].contents[1].contents[0].contents[0].contents[0].string)
    print(work)


    try:
        find_city = []
        find_city = soup.findAll('table')
        current_city = find_city[5].a.text.strip()
    except:
        current_city = ""
    print(current_city)


    per = Person(str(name), current_city, work)
    per.show()
    per.add(username)


    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(3)

    driver.get("https://m.facebook.com/" + username + "/about")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="mobile_login_bar"]/div[2]/a[2]').click()
    email = driver.find_element_by_id("m_login_email")
    passwd = driver.find_element_by_id("m_login_password")
    email.send_keys(fb_cred.email)
    passwd.send_keys(fb_cred.password)
    passwd.send_keys(Keys.RETURN)
    time.sleep(10)


    SCROLL_PAUSE_TIME = 2


    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[contains(text(),'Likes')]/../../div[3]/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/header/div/div/div[3]/a').click()
    time.sleep(3)
    favorites = []
    for span in driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div/div[1]/div[*]/div/span'):
        favorites.append(span.text)
    for span in driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[2]/div[*]/div/span'):
        favorites.append(span.text)


    if len(favorites) == 0:
        print("There are no favorites")
    else:
        print("Favorites are:")
        for i in favorites:
            print(i, end=' | ')


    driver.quit()


#scrap("radhikagarg1601")



