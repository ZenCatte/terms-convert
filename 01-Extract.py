# 原文件两列采用制表符分隔，直接将text文件装换为电子表格XLSX

import pandas as pd
# 如果报错，请安装pandas库，代码 pip install pandas

# Load the file content into a pandas DataFrame with tab as delimiter
df = pd.read_csv("files/terms.txt",
                 sep="\t",
                 names=["Chinese", "English"],
                 encoding="utf-8")

# Drop rows where both columns are empty
df = df.dropna(how="all")

# Save the DataFrame to an Excel file
output_path = "files/terms_cleaned.xlsx"
df.to_excel(output_path, index=False)

output_path
