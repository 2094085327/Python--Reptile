# 1.页面源代码
# 2.bs4解析
import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}
resp = requests.get(url, headers=headers)
print(resp.text)
# 解析
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器
list_ = page.find("list")
print(list_)

