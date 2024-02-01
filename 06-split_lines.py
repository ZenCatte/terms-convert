# 将采用制表符分隔的文本转换成电子表格
import pandas as pd
import os

# 假设我们有一些文本数据
# Read the file content
try:
    with open("files/text.txt", "r", encoding="utf-8") as file:
        text = file.readlines()
except FileNotFoundError:
    print("The file does not exist.")
    exit()

# 使用换行符分割文本，得到每一行
lines = text.split('\n')

# 确定最多的列数
max_columns = max(len(line.split('\t')) for line in lines)

# 创建一个空的DataFrame，列数为最多的列数
column_names = ['列' + str(i) for i in range(1, max_columns + 1)]
df = pd.DataFrame(columns=column_names)

# 逐行处理
for line in lines:
    # 使用空格分割每一行
    items = line.split('\t')
    # 将分割后的数据添加到DataFrame中，填充缺失的列为NaN
    df = df._append(pd.Series(items + [None] * (max_columns - len(items)), index=column_names), ignore_index=True)

# 显示DataFrame
print(df)
df.to_excel('files/output.xlsx', index=False)
