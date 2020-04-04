import os

import requests
import time
import xlwt
from lxml import etree
import requests
import time
import json
from multiprocessing.dummy import Pool as ThreadPool
import sys
from fake_useragent import UserAgent
sys.getdefaultencoding()
global html
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
cookies = '_xsrf=5rGmuL16Wlzxkd4DLf3zLpQGQfXHKx5t; cap_id=MTRmN2Y5OTJkNDM2NGE2ZWE0ZmYxYmFjOWI4MGU3ZjA=|1562420126|6b0188ec972c8e9bc0ece52545403a02ca542242; z_c0=Mi4xd2hGT0NBQUFBQUFBQUswZFZmT3hEeGNBQUFCaEFsVk5vdkVOWGdDZDNyM0FLVktHSEIxSG10TGF5ckViWmVrM0tn|1562420130|722eaede1a440e089a6530b9e64c150f987ec516; l_cap_id=ZjczN2Y1YzIyYmYxNDY0Yzk4MGU2ZDVlYjI0NjI1Y2E=|1562420126|df1c419fb4377c8d0966888228c55e3fd4ae4ae0; r_cap_id=ZDY0ZmI3N2FiZDhmNDgyNzkxNTUwZDI5MTJkMzMzYzY=|1562420126|8ae38a7f1d7e63f4e9b09f64a5b28c6c11ea6c60; tst=r; d_c0=AACtHVXzsQ-PTmvZG1-Atw8pBJbtdKTHWu4=|1562420094; capsion_ticket=2|1:0|10:1562420117|14:capsion_ticket|44:ZDJkYTBiODM2MjI2NGE5NGJkMTUxMjNhY2Y4MjQxMzY=|0d9a2399fd08b4f510e9fa3121782dccc886a850b4406e48534a2c58403fee49; _zap=5048bd66-12ab-4a1e-9c9b-6c0b5ce4b0e0; tgw_l7_route=6936aeaa581e37ec1db11b7e1aef240e'
headers = {'User-Agent': user_agent ,
           "Cookie": cookies
           }

cnt = 0
# 写表头
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('my worksheet', True)
list_class = ['name', 'headline', 'description', 'business', 'locations', 'educations']
for i in range(len(list_class)):
    sheet.write(0, i, list_class[i])


u = open("test3.html", "r", encoding='utf-8')
token = u.readlines()
for j in range(len(token)):
    token[j] = token[j].rstrip("\n")
u.close()
r = open("user_urls.txt", "r", encoding="utf-8")
usersurl = r.readlines()
for i in range(len(usersurl)):
    usersurl[i] = usersurl[i].rstrip("\n")
r.close()

for k in range(len(usersurl)):
    print("这是url:" + usersurl[k])
    print("这是token：" +  token[k])
    try:
        html = requests.get(usersurl[k],headers = headers)
    except requests.exceptions.URLRequired:
        print("URLerror")
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//script[@id = "js-initialData"]/text()')[0]
    data = json.loads(content_field)

    if data:
        # try:
        if 'name' in data['initialState']['entities']['users'][token[k]].keys():
            n = data['initialState']['entities']['users'][token[k]]['name']
        if data['initialState']['entities']['users'][token[k]]['headline']:
            h = data['initialState']['entities']['users'][token[k]]['headline']
        else:
            h = "null"
        if data['initialState']['entities']['users'][token[k]]['description']:
            d = data['initialState']['entities']['users'][token[k]]['description']
        else:
            d = "null"
        if 'name' in data['initialState']['entities']['users'][token[k]]['business'].keys():
            if data['initialState']['entities']['users'][token[k]]['business']['name']:
                b = data['initialState']['entities']['users'][token[k]]['business']['name']
        else:
            b = "null"
        if data['initialState']['entities']['users'][token[k]]['locations']:
            if 'name' in data['initialState']['entities']['users'][token[k]]['locations'][0].keys():
                l = data['initialState']['entities']['users'][token[k]]['locations'][0]['name']
        else:
            l = "null"
        if data['initialState']['entities']['users'][token[k]]['educations']:
            if 'name' in data['initialState']['entities']['users'][token[k]]['educations'][0].keys():
                e = data['initialState']['entities']['users'][token[k]]['educations'][0]['name']
        else:
            e = "null"
        lis_content = [n, h, b, l, e, d]
        print(lis_content)
        for char in l:
            if char == "台":
                for i in range(len(list_class)):
                    a = a

        for i in range(len(list_class)):
            sheet.write(cnt, i, lis_content[i])
        # except:
        #     pass
        cnt += 1
    else:
        pass

workbook.save('data.xls')