#导入必要的库
import requests
import json
import hashlib

# 百度翻译API的URL
url = "https://fanyi-api.baidu.com/api/trans/vip/translate"

# 百度翻译API密钥和APP ID
appid = '20190619000308735'
secretKey = '1N_IzdCjfCHrcjiLmIze'

# 函数：根据输入的文本自动选择翻译的方向
def translate_text(text, appid, secretKey, from_lang='auto', to_lang='auto'):
    # 计算签名
    salt = '12345'
    sign = hashlib.md5((appid + text + salt + secretKey).encode()).hexdigest()

    # 发送翻译请求
    params = {
        'appid': appid,
        'q': text,
        'from': from_lang,
        'to': to_lang,
        'salt': salt,
        'sign': sign
    }
    response = requests.get(url, params=params)

    # 解析响应
    trans_result = json.loads(response.text)
    translated_text = trans_result['trans_result'][0]['dst']
    return translated_text

# 用户输入文本
text = input("请输入文本：")

# 判断输入的文本第一个字符是英文还是中文
first_char = text[0]
def is_chinese_char(first_char):
    return '\u4e00' <= first_char <= '\u9fff'
if is_chinese_char(first_char):
    # 如果第一个字符是中文，翻译成英文
    translated_text = translate_text(text, appid, secretKey, from_lang='zh', to_lang='en')
else:
    # 如果第一个字符是英文字母，翻译成中文
    translated_text = translate_text(text, appid, secretKey, from_lang='en', to_lang='zh')

print(translated_text)
