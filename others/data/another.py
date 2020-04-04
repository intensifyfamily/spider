import os
import xlwt
from lxml import etree
import requests
import time
import json
from multiprocessing.dummy import Pool as ThreadPool
import sys
from fake_useragent import UserAgent
sys.getdefaultencoding()

ua = UserAgent()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
cookies = '_xsrf=4OtP5SdHdHrvZUoJQtTTKLCcqN0rTmBk; _zap=2c0d3df5-7c61-4a4f-8a08-087924698246; d_c0="AIAt7BDzsQ-PTuj19h6SZG0ZDJYGEcLYnfU=|1562420025"; tgw_l7_route=578107ff0d4b4f191be329db6089ff48; capsion_ticket="2|1:0|10:1562480984|14:capsion_ticket|44:M2MzM2IyY2FhOGRkNDJjNTgwYzQ2MmM0NzE0OTM2ODI=|710ddcfc5b98efbef89c4ec40569a7b70f66e425374e32623834ae346bbb9ea6"; l_n_c=1; r_cap_id="NDExZDk5ZGM1Y2Q5NDI0NzkzNGM2NjI2NzVhODRhNzE=|1562480992|e658afd7f1cfc20ec1234e88fb4b201c6c45e9d0"; cap_id="NzhlZDNmYzk2NWMzNDY0OGI5Y2IxZjE4NjdjZTAyNWY=|1562480992|49d4a256c1bd8a4109f2bd2c2d6d56f8f47f2872"; l_cap_id="MDU5NDE3M2EzZjY4NGU2MDhhODExMjExMTA1NTEwMjU=|1562480992|7561c84859ce0d281dc8ea224406483a041bfeab"; n_c=1; z_c0=Mi4xd2hGT0NBQUFBQUFBZ0Mzc0VQT3hEeGNBQUFCaEFsVk5iTjhPWGdDb3VXOHA4Y3JYVS1IREZQcUswN1ZjcXJtdHdn|1562481004|1fb5c2b97ae1cb3e02a151b64d62b7a9200e65d8'
headers = {'User-Agent': user_agent ,
           "Cookie": cookies
           }

def get_json(user_url):
    global response
    time.sleep(5)
    print(user_url)
    try:
        response = requests.get(user_url,headers = headers)
    except requests.exceptions.URLRequired:
        print("URLerror")
    f.write(response.text)
    f.write(",")


def get_user_url():
    w = open("test2.html", "r", encoding='utf-8')
    u = open("test3.html", "a+", encoding='utf-8')
    response = w.read()
    cnt = 0
    data = json.loads(response.replace('&quot',""))
    for j in range(len(data['all'])):
        for i in range(len(data['all'][j]['data'])):
            if data['all'][j]['data'][i]['url']:
                user_url = data['all'][j]['data'][i]['url']
                url_token = data['all'][j]['data'][i]['url_token']
                u.writelines(url_token + "\n")
                r.writelines(user_url + "\n")
            else:
                pass
            cnt = cnt + 1
    w.close()
    u.close()


def get_message(k):
    global html
    #处理token后面的换行符
    u = open("test3.html", "r", encoding='utf-8')
    token = u.readlines()
    for j in range(len(token)):
        token[j] = token[j].rstrip("\n")
    u.close()
    # 处理url后面的换行符
    r = open("user_urls.txt", "r", encoding="utf-8")
    usersurl = r.readlines()
    for i in range(len(usersurl)):
        usersurl[i] = usersurl[i].rstrip("\n")
    r.close()


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
        else:
            n = "null"
        if 'headline' in data['initialState']['entities']['users'][token[k]].keys():
            if data['initialState']['entities']['users'][token[k]]['headline']:
                h = data['initialState']['entities']['users'][token[k]]['headline']
            else:
                h = "null"
        else:
            h = "null"
        if 'description' in data['initialState']['entities']['users'][token[k]].keys():
            if data['initialState']['entities']['users'][token[k]]['description']:
                d = data['initialState']['entities']['users'][token[k]]['description']
            else:
                d = "null"
        else:
            d = "null"
        if 'business' in data['initialState']['entities']['users'][token[k]].keys():
            if 'name' in data['initialState']['entities']['users'][token[k]]['business'].keys():
                if data['initialState']['entities']['users'][token[k]]['business']['name']:
                    b = data['initialState']['entities']['users'][token[k]]['business']['name']
                else:
                    b = "null"
            else:
                b = "null"
        else:
            b = "null"
        if 'locations' in data['initialState']['entities']['users'][token[k]].keys():
            if data['initialState']['entities']['users'][token[k]]['locations']:
                if 'name' in data['initialState']['entities']['users'][token[k]]['locations'][0].keys():
                    l = data['initialState']['entities']['users'][token[k]]['locations'][0]['name']
                else:
                    l = "null"
            else:
                l = "null"
        else:
            l = "null"
        if 'educations' in data['initialState']['entities']['users'][token[k]].keys():
            if data['initialState']['entities']['users'][token[k]]['educations']:
                if 'name' in data['initialState']['entities']['users'][token[k]]['educations'][0].keys():
                    e = data['initialState']['entities']['users'][token[k]]['educations'][0]['name']
                else:
                    e = "null"
            else:
                e = "null"
        else:
            e = "null"
        lis_content = [n, h, b, l, e, d]
        print(lis_content)
        for char in l:
            if char == "烟":
                pass
            if char == "茅":
                pass
            if char == "台":
                for i in range(len(list_classT)):
                    sheetT.write(k, i, lis_content[i])
        for i in range(len(list_class)):
            sheet.write(k, i, lis_content[i])

    else:
        pass




if __name__ == '__main__':
    if (os.path.exists("test1.html")):
        os.remove("test1.html")
    if (os.path.exists("test2.html")):
        os.remove("test2.html")
    if (os.path.exists("test3.html")):
        os.remove("test3.html")
    if (os.path.exists("user_urls.txt")):
        os.remove("user_urls.txt")
    if (os.path.exists("data.xls")):
        os.remove("data.xls")
    if (os.path.exists("dataT.xls")):
        os.remove("dataT.xls")
    pool = ThreadPool(8)
    page = []


    # 写表头1
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('my worksheet', True)
    list_class = ['name', 'headline', 'description', 'business', 'locations', 'educations']
    for i in range(len(list_class)):
        sheet.write(0, i, list_class[i])
    # 写表头2
    workbookT = xlwt.Workbook(encoding='utf-8')
    sheetT = workbookT.add_sheet('my worksheet', True)
    list_classT = ['name', 'headline', 'description', 'business', 'locations', 'educations']
    for i in range(len(list_classT)):
        sheetT.write(0, i, list_classT[i])


    f = open("test1.html", "a+", encoding='utf-8')
    w = open("test2.html", "a+", encoding='utf-8')
    r = open("user_urls.txt","a+", encoding='utf-8')

    #从关注的人存url
    # # 这里修改人数       1021——19021 or  中间这个树减去21要是500的倍数！
    for i in range(20, 1021, 500):
        url_1 = "https://www.zhihu.com/api/v4/members/sapereaude/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset="
        url_2 = "&limit="
        newpage = url_1 + str(i) + url_2 +"500"
        page.append(newpage)
    results = pool.map(get_json, page)
    f.close()
    with open("test1.html", 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
    f = open("test1.html", "r", encoding='utf-8')
    json_all = f.read()
    w.write("{\"all\":[")
    w.write(json_all)
    w.write("]}")
    w.close()
    get_user_url()
    r.close()

    #多线程get_message
    index = []
    r = open("user_urls.txt", "r", encoding="utf-8")
    all = len(r.readlines())
    for w in range(all):
        index.append(w)
    r.close()
    print(index)
    results = pool.map(get_message, index)
    pool.close()
    pool.join()
    f.close()
    workbook.save('data.xls')
    workbookT.save('dataT.xls')












