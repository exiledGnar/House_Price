import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('D:/Pycharm/house_train/house_train_normalized.xlsx')

# 获取最后一列的列名
last_column = df.columns[-1]

# 将0-1的区间平均划分成10份，得到每个区间的中值
bins = pd.cut(df.iloc[:, -1], bins=10, labels=False) * 0.1 + 0.05

# 用中值代替所有区间内的值
df.iloc[:, -1] = bins

# 绘制直方图
plt.hist(df.iloc[:, -1], bins=10)
plt.xlabel('Discretized Values')
plt.ylabel('Frequency')
plt.title('Histogram of Discretized Values')
plt.show()

# 保存变换后的Excel文件
df.to_excel('D:/Pycharm/house_train/house_train_discretized.xlsx', index=False)