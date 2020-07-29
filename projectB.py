import pandas as pd
import time
pd.get_option('display.width')
pd.set_option('display.width',180)
# 数据加载

data = pd.read_csv('E:\Data_Engine_with_Python-master\\1.csv',encoding='gbk')
print(data)
def rule1():
	from efficient_apriori import apriori
	start = time.time()
	# 得到一维数组orders_series，并且将Transaction作为index, value为Item取值
	orders_series = data.set_index('客户ID')['产品ID']
	# 将数据集进行格式转换
	transactions = []
	temp_index = 0
	for i, v in orders_series.items():
		if i != temp_index:
			temp_set = set()
			temp_index = i
			temp_set.add(v)
			transactions.append(temp_set)
		else:
			temp_set = set()
			temp_set.add(v)
	
	# 挖掘频繁项集和频繁规则
	itemsets, rules = apriori(transactions, min_support=0.01,  min_confidence=0.2)
	itemsets = pd.DataFrame(itemsets)
	rules = pd.DataFrame(rules)
	print('频繁项集：', itemsets)
	print('关联规则：', rules)
	itemsets.to_excel('频繁项集.xlsx')
	rules.to_excel('关联规则.xlsx')   
	end = time.time()
	print("本次用时：", end-start)
# rule1()
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