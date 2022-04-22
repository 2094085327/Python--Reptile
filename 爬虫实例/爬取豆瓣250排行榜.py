# 拿到页面源代码
#  通过re来提取
import re
import requests
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"}
page = 0
while page <= 250:

    url = f"https://movie.douban.com/top250?start={page}&filter="
    resp = requests.get(url, headers=headers)
    # 页面源代码
    page_content = resp.text
    # 解析数据
    obj = re.compile(
        r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?<span class="title">&nbsp;/&nbsp;(?P<EnglishName>.*?)</span>.*?<p class="">.*?<br>(?P<Year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<Num>.*?)</span>.*?<span>(?P<People>.*?)</span>',
        re.S)
    ret = obj.finditer(page_content)
    f = open("date.csv", mode="a", encoding="utf-8")
    csvwriter = csv.writer(f)
    for i in ret:
        print("电影名:", i.group("title"))
        print("别称:", i.group("EnglishName"))
        print("年份:", i.group("Year").strip())
        print("评分:", i.group("Num").strip())
        print("评价人数:", i.group("People").strip())
        print(" ")
        dic = i.groupdict()
        dic["Year"] = dic["Year"].strip()
        dic["Num"] = dic["Num"].strip()
        dic["People"] = dic["People"].strip()
        csvwriter.writerow(dic.values())
    page += 25
    resp.close()
    f.close()
