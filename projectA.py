import requests
from bs4 import BeautifulSoup
import pandas as pd
# 请求URL
url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text
soup = BeautifulSoup(content,'html.parser')
temp = soup.find('div',class_='search-result-list')


df= pd.DataFrame(columns=['名称','价格','产品图片链接'])
p_list = temp.find_all('p')
print(temp)


temp2={}
images = temp.find_all('img')
for image in images:
    
    temp2['产品图片链接']=image['src']
    

name = soup.find_all('p',class_='cx-name text-hover')
price = soup.find_all('p',class_='cx-price')


for i in range(len(name)):
    
    temp2['名称']=name[i].string
    temp2['价格']=price[i].string
    # temp2['产品图片链接']=pic[i]
    df=df.append(temp2,ignore_index=True)
df['最高价格']=df['价格']
df['最低价格']=df['价格']
df['最高价格']=df['最高价格'].str.split('-',expand=True)[1]
df['最低价格']=df['最低价格'].str.split('-',expand=True)
df.drop(columns=['价格'],inplace=True)
print(df)
df.to_excel('E:\\python_project\\GIT\\DATA_ANALYSIS\\test\\test\\SUV清单.xlsx')