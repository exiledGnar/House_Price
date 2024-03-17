import pandas as pd
import matplotlib.pyplot as plt

excel_path = 'D:/Pycharm/house_train/house_train_num.xlsx'

# 读取Excel文件
data = pd.read_excel(excel_path)

# 删除"price"列中值在700以上的数据所在行
data_filtered = data[data['price'] < 700]

# 绘制直方图并保存为PDF
plt.figure(figsize=(10, 6))
plt.hist(data_filtered['price'], bins=20)
plt.title("Price Histogram (Filtered)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.savefig('D:/Pycharm/house_train/price_histogram_filtered.pdf', format='pdf')
plt.show()

# 保存过滤后的数据为Excel文件
output_path = r'D:/Pycharm/house_train/house_train_filtered.xlsx'
data_filtered.to_excel(output_path, index=False)

print("已删除值在700以上的数据所在行，并保存为Excel文件。")