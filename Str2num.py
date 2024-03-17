import pandas as pd

excel_path = r'D:/Pycharm/house_train/house_train_filtered.xlsx'

# 读取Excel文件
data = pd.read_excel(excel_path)

# 定义替换规则字典
replace_dict = {'Low': 0, 'Medium': 0.5, 'High': 1}

# 替换"floor"列的元素
data['floor'] = data['floor'].replace(replace_dict, regex=True)

# 提取"built_date"列的年份信息
data['built_date'] = pd.to_datetime(data['built_date']).dt.year

# 保存更新后的Excel文件
output_path = r'D:/Pycharm/house_train/house_train_num.xlsx'
data.to_excel(output_path, index=False)

print("已进行替换操作，并保存为新的Excel文件。")