from selenium import webdriver
import pandas as pd 
import time

browser = webdriver.Chrome('C:\\Users\\DELL PC\\Desktop\\chromedriver.exe')
browser.get('https://www.worldometers.info/coronavirus/')
time.sleep(10)

column_names = ['Rank','Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths','Recovered', 'Active Cases', 'Critical']
df = pd.DataFrame(columns = column_names)
print(df)
filename = input('Enter the file name to store the data: ')
print('Filename is '+filename)
for i in browser.find_elements_by_xpath('//*[@id = "main_table_countries_today"]/tbody/tr'):
	td_list = i.find_elements_by_tag_name('td')
	row = []
	for td in td_list:
		row.append(td.text)
	data = {}
	for j in range(len(df.columns)):
		data[df.columns[j]] = row[j]
	df = df.append(data, ignore_index = True)

df = df.iloc[1:]
print(df)


path = 'D:\\alienbrains\\'+filename+'.csv'
df.to_csv(path,index=False)
print("The dataset has been saved at the location: "+path)