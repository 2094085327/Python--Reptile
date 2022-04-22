# 定位到子页面
# 提取到子页面的链接地址
# 请求连接地址，拿到需要的下载数据
import requests
import re

domain = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"}
resp = requests.get(domain, headers=headers, verify=False)  # verify=False 去掉安全验证,绕过部分加密
resp.encoding = "gb2312"  # 指定字符集（重新编码）
page_content = resp.text
obj = re.compile(r'2022必看热片.*?<ul>(?P<title>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<herf>.*?)'", re.S)
obj3 = re.compile(
    r'◎片　　名　(?P<download>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<conect>.*?)">',
    re.S)
ret = obj.finditer(page_content)
# 保存子页面连接
child_href_list = []
for i in ret:
    # print(i.group("title"))
    ul = i.group("title")
    ret2 = obj2.finditer(ul)
    # 提取子页面连接
    for it in ret2:
        # 拼接URL连接
        child_href = domain + it.group("herf").strip("/")
        # print(it.group("herf"))
        # print(child_href)
        child_href_list.append(child_href)
        print(" ")

for href in child_href_list:
    child_resp = requests.get(href, headers=headers)  # , verify=False
    child_resp.encoding = "gbk"
    ret3 = obj3.finditer(child_resp.text)
    for ittt in ret3:
        print("片名：", ittt.group("download"))
        print("连接：", ittt.group("conect"))
        print(" ")
    child_resp.close()
resp.close()
