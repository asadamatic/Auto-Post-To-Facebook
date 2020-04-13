from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from getpass import getpass
import sys
import time


option = Options()

#Adding attributes to the browser to be openned
option.add_argument('start-maximized')
option.add_argument('--disable-extensions')
option.add_argument('--disable-notifications')

#Click 'Block' option on browser notification that asks for 'Push notifications' permission
option.add_experimental_option('prefs', { 'profile.default_content_setting_values.notifications': 2})   

print('Provide your login credentials!')
username = input('Enter your username: ')
password = getpass()

status = input('Enter your message: ')

browser = webdriver.Chrome(options=option)

browser.get('https://www.facebook.com')

delay = 5

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

    time.sleep(4)
    if browser.current_url ==  'https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110':

        print('Wrong Credentials :(')
        sys.exit() #exit the program

    else:

        print('Successfuly Loggedin :)')  
          

except (NoSuchElementException, TimeoutException) as exception:

    print("Slow Or No Connection :(")
    sys.exit()




try:

    """ For older facebook ui """

    #Waiting for the "What's on your mind?" text box t obe clickable and then creating a reference for it
    createPost = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='xhpc_message']")))

    createPost.send_keys(status)

    print('Writing Status..')

except (TimeoutException, NoSuchElementException):

    try:

        """ For new facebook ui """

        #Waiting for the "What's on your mind?" text box t obe clickable and then creating a reference for it
        createPost = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0"]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div[1]')))
        createPost.click()

        time.sleep(3)

        writePost = browser.switch_to.active_element

        time.sleep(3)
        writePost.send_keys(status)                                         
        

        print('Writing Status..')

    except (TimeoutException, NoSuchElementException):

        print('Slow Or No Connection :(')
        sys.exit()
    

try:

    """ For older facebook ui """

    #Waiting for "Post" button to be clickable 
    postButton = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button/span[.=\"Post\"]")))

    postButton.click()

    print('Status Posted Successfully :)')
    
    
except (TimeoutException, NoSuchElementException):

    try:

        """ For new facebook ui """

        #Waiting for "Post" button to be clickable 
        postButton = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="facebook"]/body/div[9]/div/div/div[2]/div/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div')))
                                                                                        
        postButton.click()

        print('Status Posted Successfully :)')

    except:
        print('Slow Or No Connection :(')
        sys.exit()
