import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取 Excel 文件
data = pd.read_excel(r'D:/Pycharm/house_train/house_train_discretized.xlsx')

# 提取特征列
features = ['area', 'built_date', 'green_rate', 'traffic', 'floor', 'oriented', 'shockproof', 'school', 'crime_rate', 'pm25', 'price']
data = data[features]

# 计算相关系数
correlation_matrix = data.corr()

# 绘制热图
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Coefficient Heatmap')

# 保存为 PDF
plt.savefig('correlation_heatmap.pdf', format='pdf')