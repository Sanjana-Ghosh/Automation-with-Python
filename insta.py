from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\\DELL PC\\Desktop\\chromedriver.exe')

user_profile = input("Enter the profile name: ")
browser.get('https://www.instagram.com/'+user_profile)

try:
	img = browser.find_element_by_xpath('//img[@class="_6q-tv"]')
	
except:
	img = browser.find_element_by_xpath('//img[@class="be6sR"]')


img_link = img.get_attribute('src')
path = 'D:\\alienbrains\\'+user_profile+'.jpg'

import urllib.request

urllib.request.urlretrieve(img_link,path)


print("The profile pic has been downloaded at: "+path)

browser.quit()