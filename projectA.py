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

print(temp)
df= pd.DataFrame(columns=['名称','价格','产品图片链接'])
p_list = temp.find_all('p')
print(p_list)
for rows in p_list:
    temp2={}
    name= rows[1]
    price= rows[2]
    temp2['名称'],temp2['价格']=name,print
#     temp2={}
#     p2_list=p_list.find_all('p')
 
#     名称,价格=p2_list[0],p2_list[1]
#     temp2['名称'],temp2['价格']=名称,价格
    df=df.append(temp2,ignore_index=True)
print(df)
