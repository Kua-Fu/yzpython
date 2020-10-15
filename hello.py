# -*- coding:utf-8 -*-

print("hello, world!")

import requests

res = requests.get("https://www.baidu.com")

print(res.status_code, res.text)
