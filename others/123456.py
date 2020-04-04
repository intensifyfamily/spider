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
all_url = []

ua = UserAgent()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

cookie = 'q_c1=70060403e22b4d7980caa6d4eed05e31|1562336344|1562336344; _zap=b942f5c4-ff5b-4c31-aaf0-5e0d1125bc71; _xsrf=SPs1v9NYQThjqkjS3M0yB6PNfQVppmyS; d_c0="ALDtP7GzsA-PTqdAjLn_eSN0PtY9oV4zDAA=|1562336303"; capsion_ticket="2|1:0|10:1562336306|14:capsion_ticket|44:NjJmZDJkYWIxODI5NDk3NzlkM2MxYjgyOWY3YjBkMDE=|4fad4eb6369968e12d573968eb0b09186385d892e8516b6d5c5558dcdb6959c6"; z_c0="2|1:0|10:1562336342|4:z_c0|92:Mi4xd2hGT0NBQUFBQUFBc08wX3NiT3dEeVlBQUFCZ0FsVk5WcW9NWGdEYU9aYjBNQ3FDYVExU1BEa0JuemE1SzY0N2lR|65cbfa769ff9f675bf5de3db089dc663d98ebae58f5c34444327051f924b4da2"; q_c1=e7021d266b394eb5833b57c85c732da3|1562336638000|1562336638000; tshl=; tst=f; tgw_l7_route=578107ff0d4b4f191be329db6089ff48'


def get_user_url(user_url):
    # print(user_url)
    global response
    # for each in user_url:
    time.sleep(5)
    headers = {'User-Agent': user_agent }
    print(user_url)
    try:
        response = requests.get(user_url,headers = headers)
    except requests.exceptions.URLRequired:
        print("URLerror")

    data = json.loads(response.text)
    # print(u)
    print(data)
    print(data['data'])
    for x in range(len(data['data'])):
        if data['data'][x]['target']['author']['url_token']:
            url_token = data['data'][x]['target']['author']['url_token']
            url = "https://www.zhihu.com/people/" + url_token
            all_url.append(url)
        else:
            pass



if __name__ == '__main__':
    pool = ThreadPool(8)
    page = []
    for i in range(9, 110, 10):
        url_1 = "https://www.zhihu.com/api/v3/feed/topstory/follow_wonderful?action=down&session_token=947820136fd8e310675d17d7e8e65430FW&limit=7&after_id="
        url_2 = "&desktop=true"
        newpage = url_1 + str(i) + url_2
        page.append(newpage)

    # print(page)
    results = pool.map(get_user_url,page)
    pool.close()
    pool.join()
    print(len(all_url))




















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




