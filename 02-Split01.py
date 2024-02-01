# 中文在前英文在后的句段（不存在制表符或分隔符），分割成两列，并保存成电子表格
# Import necessary library for regular expressions
import pandas as pd

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
print


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

# Save the DataFrame to an Excel file
output_path = "files/terms_split01.xlsx"
df.to_excel(output_path, index=False)
