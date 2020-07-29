# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
#data = pd.read_csv('Mall_Customers.csv', encoding='gbk')
data = pd.read_csv('E:\Data_Engine_with_Python-master\\c.csv')
train_x = data[["car_ID","enginesize","price","carlength"]]

# LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train_x['car_ID'] = le.fit_transform(train_x['car_ID'])

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
#print(train_x)


### 使用KMeans聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("E:\Data_Engine_with_Python-master\\customer_cluster_result.csv",index=False)


