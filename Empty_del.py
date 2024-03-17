import pandas as pd

excel_path = r'D:/Pycharm/house_train/house_train.xlsx'

# 读取Excel文件
data = pd.read_excel(excel_path)

# 检测缺失值
missing_values = data.isnull().any(axis=1)

# 删除包含缺失值的行
data = data[~missing_values]

# 保存处理后的Excel文件
output_path = r'D:/Pycharm/house_train/house_train_del.xlsx'
data.to_excel(output_path, index=False)

print("已删除包含缺失值的行，并保存为新的Excel文件。")