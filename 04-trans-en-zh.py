import requests
import json
import hashlib

# 百度翻译API的URL
url = "https://fanyi-api.baidu.com/api/trans/vip/translate"

# 您的API密钥和APP ID
appid = '20190619000308735'
secretKey = '1N_IzdCjfCHrcjiLmIze'

# 要翻译的文本和目标语言

q = input("请输入英文：")  # 要翻译的文本
from_lang = 'en'  # 源语言
to_lang = 'zh'  # 目标语言

# 计算签名
salt = '12345'
sign = hashlib.md5((appid + q + salt + secretKey).encode()).hexdigest()

# 发送翻译请求
params = {
    'appid': appid,
    'q': q,
    'from': from_lang,
    'to': to_lang,
    'salt': salt,
    'sign': sign
}
response = requests.get(url, params=params)

# 解析响应
trans_result = json.loads(response.text)
translated_text = trans_result['trans_result'][0]['dst']
print(translated_text)
