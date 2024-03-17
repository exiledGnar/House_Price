import pandas as pd

csv_path = r'D:/Pycharm/house_train/house_train.csv'
excel_path = r'D:/Pycharm/house_train/house_train.xlsx'

# 读取CSV文件
data = pd.read_csv(csv_path)

# 将数据保存为Excel文件
data.to_excel(excel_path, index=False)

print("CSV文件已成功转换为Excel文件。")