from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import getpass
import sys

print('Provide your login credentials!')
username = input('Username: ')
password = getpass.getpass()

status = input("What's on your mind?\n")

browser = webdriver.Chrome(executable_path = 'D:\Programming Languages\Python Accessories\chromedriver_win32\chromedriver.exe')

browser.maximize_window()

browser.get('https://www.facebook.com')

delay = 3

wait = WebDriverWait(browser, delay)

try:
    #Referencing text box that asks for email
    usernameInput = browser.find_element_by_xpath('//*[@id="email"]')
    usernameInput.send_keys(username)
    
    #Referencing text box that asks for password
    passwordInput = browser.find_element_by_xpath('//*[@id="pass"]')
    passwordInput.send_keys(password)

    #Referencing Login Button
    loginButton = browser.find_element_by_xpath('//*[@id="loginbutton"]')
    loginButton.click()

    if browser.current_url ==  'https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110':

        print('Wrong Credentials :(')
        sys.exit() #exit the program

    else:

        print('Successfuly Loggedin :)')       

except (NoSuchElementException, TimeoutException) as exception:

    print("Slow Or No Connection :(")
    sys.exit()




try:

    delay = 2

    wait = WebDriverWait(browser, delay)

    #Waiting for the "What's on your mind?" text box t obe clickable and then creating a reference for it
    createPost = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='xhpc_message']")))

    createPost.send_keys(status)

    print('Writing Status..')

except (NoSuchElementException, TimeoutException) as exception:

    print('Slow Or No Connection :(')
    sys.exit()


try:
    delay = 4

    wait = WebDriverWait(browser, delay)

    #Waiting for "Post" button to be clickable 
    postButton = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button/span[.=\"Post\"]")))

    postButton.click()

    print('Status Posted Successfully :)')
except (NoSuchElementException, TimeoutException) as exception:

    print('Slow Or No Connection :(')
    sys.exit()