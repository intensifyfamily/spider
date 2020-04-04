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
# data_target_author_url_token
#next: "https://www.zhihu.com/api/v3/feed/topstory/follow_wonderful?action=down&session_token=947820136fd8e310675d17d7e8e65430FW&limit=7&after_id=59&desktop=true"
# all_url = []

ua = UserAgent()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
headers = {'User-Agent': user_agent }

def get_json(user_url):
    global response
    time.sleep(5)
    print(user_url)
    try:
        response = requests.get(user_url,headers = headers)
    except requests.exceptions.URLRequired:
        print("URLerror")
    f.write(response.text + ",")


def get_user_url():

    response = f.read().split("tangjiangspid")
    cnt = 0
    for x in response:
        print(x)
        data = json.loads(x)
        for i in range(len(data['data'])):
            if data['data'][i]['url']:
                user_url = data['data'][x]['url']

                f.writelines(user_url)
            else:
                pass
        cnt = cnt + 1
        print(cnt)


# initialState+entities+users+jeffreycheung+name
# initialState+entities+users+jeffreycheung+headline
# initialState+entities+users+jeffreycheung+description
# initialState+entities+users+jeffreycheung+business+name
# initialState+entities+users+jeffreycheung+locations[0]+name
# initialState+entities+users+jeffreycheung+educations[0]+name

def get_message():
    global html
    r = open("user_urls.txt","r")
    usersurl = r.readlines()
    for i in range(len(usersurl)):
        usersurl[i] = usersurl[i].rstrip("\n")
    cnt = 0
    for user_url in usersurl:
        url_token = user_url.rstrip("https://www.zhihu.com/people/")
        try:
            html = requests.get(user_url,headers = headers)
        except requests.exceptions.URLRequired:
            print("URLerror")
        selector = etree.HTML(html.text)
        content_field = selector.xpath('//script[@id = "js-initialData"]/text()')[0]
        data = json.loads(content_field)
        if data:
            name = data['initialState']['entities']['users'][url_token]['name']
            headline = data['initialState']['entities']['users'][url_token]['headline']
            description = data['initialState']['entities']['users'][url_token]['description']
            business = data['initialState']['entities']['users'][url_token]['business']['name']
            locations = data['initialState']['entities']['users'][url_token]['locations'][0]['name']
            educations = data['initialState']['entities']['users'][url_token]['educations'][0]['name']
        else:
            pass

        n = name
        h = headline
        d = description
        b = business
        l = locations
        e = educations
        lis_content = [n, h, b, l, e, d]
        for i in range(len(list_class)):
            sheet.write(cnt, i, lis_content[i])
        cnt += 1





if __name__ == '__main__':
    pool = ThreadPool(8)
    page = []
    #从关注的人存url
    for i in range(20, 19021, 500):
        url_1 = "https://www.zhihu.com/api/v4/members/sapereaude/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset="
        url_2 = "&limit="
        newpage = url_1 + str(i) + url_2 +"500"
        page.append(newpage)
    #写表头
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('my worksheet', True)
    list_class = ['name', 'headline', 'description', 'business', 'locations', 'educations']
    for i in range(len(list_class)):
        sheet.write(0, i, list_class[i])

    f = open("test1.html", "a+", encoding='utf-8')
    w = open("test2.html", "w", encoding='utf-8')
    results = pool.map(get_json,page)
    pool.close()
    pool.join()
    w.write("{\"all\":[" + f.read() + "]}")


    f.close()
    get_message()

    workbook.save('data.xls')

















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




