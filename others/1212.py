import requests
import re
import time
from lxml import etree
import requests
import time
import json
from multiprocessing.dummy import Pool as ThreadPool
import sys
from fake_useragent import UserAgent
sys.getdefaultencoding()
# data_target_author_url_token
#next: "https://www.zhihu.com/api/v3/feed/topstory/follow_wonderful?action=down&session_token=947820136fd8e310675d17d7e8e65430FW&limit=7&after_id=59&desktop=true"
f = open("fuck.html","r",encoding='utf-8')
w = open("user_urls.txt","a+",encoding='utf-8')
# print(f.read())
response = f.read()
# print(response)
cnt = 0
# for x in response:
#     print(x)
data = json.loads(response)
for j in range(len(data['all'])):
    for i in range(len(data['all'][j]['data'])):
        if data['all'][j]['data'][i]['url']:
            user_url = data['all'][j]['data'][i]['url']
            w.writelines(user_url + "\n")
        else:
            pass
        cnt = cnt + 1
    print(cnt)

f.close()
w.close()


















#   转utf-8
# global response
# u = "https://www.zhihu.com/api/v3/feed/topstory/follow_wonderful?action=down&session_token=947820136fd8e310675d17d7e8e65430FW&limit=7&after_id=209&desktop=true"
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# headers = { 'User-Agent' : user_agent }
# try:
#     response = requests.get(u,headers = headers)
# except requests.exceptions.URLRequired:
#     print("URLerror")
# print(response.text)


#获取urlToken
# selector = etree.HTML(html.text)
# content_field = selector.xpath('//script[@id = "js-initialData"]/text()')[0]
#
# userid = selector.xpath('//div[@class = "ContentItem AnswerItem"]')
# id = []
# for each in userid:
#     idid = each.xpath('@name')[0]
#     id.append(idid)
# allname = []
# allurl = []
# if content_field:
#     reply_info = json.loads(content_field)
#     for ids in id:
#
#         url = reply_info['initialState']['entities']['answers'][ids]['author']['urlToken']
#         allurl.append(str(url))
#     print(allurl)
# else:
#     print("fuck")
#获取urlToken结束




