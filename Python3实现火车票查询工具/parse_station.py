# coding:utf-8
"""获取火车站拼音简写"""
import re
from pprint import pprint
import requests



url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9029'

response = requests.get(url, verify=False)
response.content.decode("utf8","ignore").encode("gbk","ignore")
stations = re.findall(u'([\u4e00-\u8fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
