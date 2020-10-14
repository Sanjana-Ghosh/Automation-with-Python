from selenium import webdriver
import pandas as pd 
import time

browser = webdriver.Chrome('C:\\Users\\DELL PC\\Desktop\\chromedriver.exe')

month = 'July'
year = '2020'

browser.get('https://www.accuweather.com/en/in/mumbai/204842/'+month+'-weather/204842?year='+year+'&view=list')
time.sleep(10)

h = browser.find_elements_by_class_name("high")

high=[]
for i in h:
	t=i.get_attribute('textContent')
	high.append(int(t[:2]))
#print(high)


l = browser.find_elements_by_class_name("low")

low = []
for j in l:
	t = j.get_attribute('textContent')
	low.append(int(t[3:5]))
#print(low)

p = browser.find_elements_by_xpath("//div[@class='info precip']/p[2]")

prec = []

for k in p:
	t = k.get_attribute('textContent')
	prec.append(float(t[:3]))
#print(prec)

day = []
for l in range(len(prec)):
	day.append(l+1)

dic = {"Date":day,"High_Temperature":high, "Low_Temperature":low, "Precipitation":prec}
print(dic)

df = pd.DataFrame(dic)
print(df)
df.to_csv("D:\\alienbrains\\Mumbai_"+month+"_weather.csv",index = False)
print("File saved.")