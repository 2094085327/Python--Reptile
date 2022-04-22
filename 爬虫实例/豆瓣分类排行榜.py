import time

import requests

url = "https://movie.douban.com/j/chart/top_list"
# 重新封装参数，URL中？后面的就是参数
i = 0
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": i,
    "limit": 20
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"
}

resp = requests.get(url, params=param, headers=headers)
print(resp.json())
print(resp.request.url)
resp.close()
