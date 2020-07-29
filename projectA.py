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

name = soup.find_all('p',class_='cx-name text-hover')
price = soup.find_all('p',class_='cx-price')
pic = soup.finde_all('img',class_="img")
print(name,price,pic)