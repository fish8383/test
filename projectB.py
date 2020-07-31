import pandas as pd
import time
pd.get_option('display.width')
pd.set_option('display.width',180)
# 数据加载

data = pd.read_csv('E:\Data_Engine_with_Python-master\\1.csv',encoding='gbk')
data['订单日期']=pd.to_datetime(data['订单日期'])
data=data.sort_values(['客户ID','订单日期'],ascending=[True,True])
a=1

# 把每个客户每一次购买设定一个订单号到订单数量这一列

for i in range(len(data.iloc[:,2])-1):
	j=i+1
	
	if data.iloc[i,0]==data.iloc[j,0]and data.iloc[i,11]==data.iloc[j,11] :
		
		data.iloc[j,2]=a
		data.iloc[i,2]=a
		
		
	else:
		a=a+1
		data.iloc[j,2]=a  
# data.to_excel('E:\\python_project\\GIT\\DATA_ANALYSIS\\test\\test\\data.xlsx')
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

# 采用mlxtend.frequent_patterns工具包
def rule2():
	from mlxtend.frequent_patterns import apriori as ap
	from mlxtend.frequent_patterns import association_rules
	pd.options.display.max_columns=1000
	start = time.time()
	hot_encoded_df=data.groupby(['订单数量','产品名称'])['产品名称'].count().unstack().reset_index().fillna(0).set_index('订单数量')
	
	hot_encoded_df = hot_encoded_df.applymap(encode_units)
	print(hot_encoded_df)
	frequent_itemsets = ap(hot_encoded_df, min_support=0.01, use_colnames=True)
    
	rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.2)
   
	print("频繁项集：", frequent_itemsets)
    
	print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.3) ])
	
	rules.to_excel('E:\\python_project\\GIT\\DATA_ANALYSIS\\test\\test\\关联规则2.xlsx')
	frequent_itemsets.to_excel('E:\\python_project\\GIT\\DATA_ANALYSIS\\test\\test\\频繁项集2.xlsx')
	end = time.time()
	

rule2()