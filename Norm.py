import pandas as pd
import matplotlib.pyplot as plt

excel_path = r'D:/Pycharm/house_train/house_train_filtered.xlsx'

# 读取Excel文件
data = pd.read_excel(excel_path)

# 要归一化的列名列表
columns_to_normalize = ['built_date', 'area','green_rate', 'traffic', 'floor',
                        'oriented', 'shockproof', 'school', 'crime_rate', 'pm25', 'price']

# 归一化处理
normalized_data = (data[columns_to_normalize] - data[columns_to_normalize].min()) / \
                  (data[columns_to_normalize].max() - data[columns_to_normalize].min())

# 将归一化后的数据添加到原始数据中
data_normalized = pd.concat([data.drop(columns=columns_to_normalize), normalized_data], axis=1)

# 保存归一化后的数据为Excel文件
output_path = r'D:/Pycharm/house_train/house_train_normalized.xlsx'
data_normalized.to_excel(output_path, index=False)
"""""
# 绘制直方图并保存为PDF
for column in columns_to_normalize:
    plt.figure(figsize=(10, 6))
    plt.hist(data_normalized[column], bins=int(1 / 0.1), range=(0, 1))
    plt.xticks([i / 20 for i in range(21)])
    plt.title(f"{column} Histogram")
    plt.xlabel("Normalized Value")
    plt.ylabel("Frequency")
    plt.savefig(f'D:/Pycharm/house_train/{column}_histogram.pdf', format='pdf')
    plt.close()

print("已保存归一化后的数据为Excel文件，并绘制并保存直方图为PDF文件。")
"""""