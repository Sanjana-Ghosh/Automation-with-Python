from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\\Users\\DELL PC\\Desktop\\chromedriver.exe')

browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')


times = int(input('How many times you want to send the message?  '))
phone_number = input('Enter the mobile number:  ')

phone = browser.find_element_by_id('ap_email')
phone.send_keys(phone_number)

cnt = browser.find_element_by_id('continue')
cnt.click()

otp = browser.find_element_by_id('continue')
otp.click()

for i in range(times-1):
	send = browser.find_element_by_link_text('Resend OTP')
	send.click()

browser.quit()