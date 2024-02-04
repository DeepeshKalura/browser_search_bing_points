import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from constant import EMAIL

def get_question():
    API_URL = "https://opentdb.com/api.php?amount=90"
    questions = []
    response = requests.get(API_URL)
    data = response.json()
    for question in data["results"]:
        questions.append(question["question"])
    return questions

def openRandomFirstSearch():
    driver.get('https://www.bing.com/')
    driver.implicitly_wait(5)
    time.sleep(5)
    search_box = driver.find_element('id', 'sb_form_q')
    search_box.send_keys("Searching the best super hero")
    search_box.send_keys(Keys.RETURN)




def register():
    time.sleep(5)
    sign_in_link = driver.find_element(By.ID, "id_l")
    sign_in_link.click()
    try :
        email = driver.find_element(By.ID, "i0116")
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
        print("Please check the HTML element ID for the email input field")



try:
    driver = webdriver.Edge()
except  Exception as e:
    print(e)
    print("Please install Edge WebDriver and add it to your PATH")
    exit(1)

openRandomFirstSearch()
register()

phoneSeLink = input("Please enter the yes:   ")


if (phoneSeLink == "yes"):
    not_to_signed = driver.find_element(By.ID, "declineButton")
    not_to_signed.click()

    questions = get_question()
    for i in questions:
        search_box = driver.find_element('id', 'sb_form_q')
        search_box.clear()
        search_box.send_keys(i)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)


driver.quit()
print("Ent of the program")