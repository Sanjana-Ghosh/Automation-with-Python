from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\\Users\\DELL PC\\Desktop\\chromedriver.exe')

browser.get('https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in')

email = input('Enter the email id: ')
password = input('Enter the password: ')

usr = browser.find_element_by_id('username')
usr.send_keys(email)

pwd = browser.find_element_by_id('password')
pwd.send_keys(password)

signin = browser.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')
signin.click()

noti = browser.find_element_by_xpath('//span[@class="nav-item__badge-count"]').get_attribute("innerText")
print('Total number of unread notification is '+noti)

browser.quit()
