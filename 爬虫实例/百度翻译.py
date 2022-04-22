import requests

url = 'https://fanyi.baidu.com/sug'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}
s = input("输入需要翻译的中文:")
# 创建字典，字典中含有fromdate参数kw
dat = {
    "kw": s
}
resp = requests.post(url, data=dat)
print(resp.json())
resp.close()