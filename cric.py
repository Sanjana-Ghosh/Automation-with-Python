from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

url = 'https://www.espncricinfo.com/rankings/content/page/211271.html'
pg = urlopen(url)
soup=BeautifulSoup(pg,'html.parser')


column=[]
head = soup.find('tr',{'class':'head'})
col = head.findAll('th')
for i in col:
	j = i.text
	column.append(j)

df = pd.DataFrame(columns = column)

title = soup.findAll('h3')
name=[]
for t in title:
	name.append(t.text)


t_row = soup.findAll('tr')
n=0
for i in t_row:
	row =[]
	data = i.findAll('td')
	for d in data:
		row.append(d.text)
		dic={}
	try:
		for j in range(len(df.columns)):
			dic[df.columns[j]]=row[j]
		df.append(dic,ignore_index=True)
	except:
		df=pd.DataFrame(columns=column)
		table_name = name[n]
		n+=1
	df.to_csv('D:\\alienbrains\\CricData'+table_name+'.csv', index = False)
print("Exported to csv file")