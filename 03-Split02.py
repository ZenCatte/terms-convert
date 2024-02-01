# 加入是否存在文件的判断，如果文件存在，则以新的文件建立
# 中文在前英文在后的句段，分割成两列，并保存成电子表格

# Import necessary library for regular expressions
import pandas as pd
import os

# Read the file content
try:
    with open("files/terms-01.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
except FileNotFoundError:
    print("The file does not exist.")
    exit()

# Define a function to check if a character is Chinese
def is_chinese_char(char):
    return '\u4e00' <= char <= '\u9fff'

# Define a function to extract Chinese and English terms from a line
def extract_terms(line):
    # Find the index of the last Chinese character or punctuation
    last_chinese_index = next(
        (i for i, char in reversed(list(enumerate(line)))
         if is_chinese_char(char) or char in "，。！？；：“”）"), None)

    if last_chinese_index is not None:
        chinese_term = line[:last_chinese_index + 1]
        english_term = line[last_chinese_index + 1:].strip()
        return chinese_term, english_term
    else:
        return None, None


# Extract terms from each line
chinese_terms = []
english_terms = []

for line in content:
    chinese_term, english_term = extract_terms(line)
    if chinese_term and english_term:
        chinese_terms.append(chinese_term)
        english_terms.append(english_term)

# Check the first few terms to verify the extraction
print(chinese_terms[:5], english_terms[:5])

# Convert the Chinese and English lists into a single DataFrame
df = pd.DataFrame({"中文": chinese_terms, "英文": english_terms})

# 判断文件是否存在
# 文件名
file_name = 'terms_split01.xlsx'

# 文件路径
file_path = 'files'

# 判断文件是否存在
file_exists = os.path.isfile(os.path.join(file_path, file_name))

if not file_exists:
    # 如果文件不存在，保存文件
    # Save the DataFrame to an Excel file
    output_path = "files/terms_split01.xlsx"
    df.to_excel(output_path, index=False)
else:
    # 如果文件存在，修改文件名保存
    base, extension = os.path.splitext(file_name)
    new_file_name = f"{base}_new{extension}"
    output_path_new = os.path.join(file_path, new_file_name)
    df.to_excel(output_path_new, index=False)
