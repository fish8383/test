import pandas as pd
import time
pd.get_option('display.width')
pd.set_option('display.width',180)
# 数据加载

data = pd.read_csv('E:\Data_Engine_with_Python-master\\1.csv',encoding='gbk')
print(data)

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
	hot_encoded_df=data.groupby(['客户ID','产品ID'])['产品ID'].count().unstack().reset_index().fillna(0).set_index('客户ID')
	
	hot_encoded_df = hot_encoded_df.applymap(encode_units)
	frequent_itemsets = ap(hot_encoded_df, min_support=0.01, use_colnames=True)
    
	rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.2)
   
	print("频繁项集：", frequent_itemsets)
    
	print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.2) ])
	print(rules['confidence'])
	rules.to_excel('E:\Data_Engine_with_Python-master\\关联规则2.xlsx')
	frequent_itemsets.to_excel('E:\Data_Engine_with_Python-master\\频繁项集2.xlsx')
	end = time.time()
	print("总用时：", end-start)
rule2()