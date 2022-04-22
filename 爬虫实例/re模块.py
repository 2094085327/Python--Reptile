import re
import requests

# findall：匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+", "电话号码1：111542542，电话号码2:16463164654")
print(lst)

# finditer:匹配字符串中所有的内容[返回的是迭代器],从迭代器拿到内容需要.group()
it = re.finditer(r"\d+", "电话号码1：111542542，电话号码2:16463164654")
for i in it:
    print(i.group())

# search是找到一个结果就返回，返回对象为match对象，拿到内容需要.group()
s = re.search(r"\d+", "电话号码1：111542542，电话号码2:16463164654")
print(s.group())

# match从头开始匹配
s = re.search(r"\d+", "1：111542542，电话号码2:16463164654")
print(s.group())

# 预加载正则
obj = re.compile(r"\d+")
ret = obj.finditer("电话号码1：111542542，电话号码2:16463164654 ")
for i in ret:
    print(i.group())
ret = obj.findall("adfhadjh1289qyiewqh123431")
print(ret)

s = """
<span style="display:none" class="mac_history_set" alt="视频历史记录" data-name="[国产剧]我叫赵甲第" data-pic="https://pic.iqiyipic.com.aibaily.cn/img/upload/vod/20220331-1/5ad32db72020a790296b3578c0b4e163.jpg"></span>
<span style="display:none" class="mac_history_set" alt="视频过去记录" data-name="[港片]哈哈哈哈" data-pic="https://pic.iqiyipic.com.aibaily.cn/img/upload/vod/20220331-1/5ad32db72020a790296b3578c0b4e163.jpg"></span>
<span style="display:none" class="mac_history_set" alt="视频未来记录" data-name="[欧美]咦嘻嘻嘻" data-pic="https://pic.iqiyipic.com.aibaily.cn/img/upload/vod/20220331-1/5ad32db72020a790296b3578c0b4e163.jpg"></span>
"""
# (?P<名字>正则)可以单独从正则匹配的内容中获取需要的部分
obj2 = re.compile(r"alt=(?P<one>.*?)data-name=(?P<two>.*?)data", re.S)
ret2 = obj2.finditer(s)
for i in ret2:
    print(i.group("one"))
    print(i.group("two"))
