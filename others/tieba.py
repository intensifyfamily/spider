#https://tieba.baidu.com/p/6117888348?pn=1
#d_post_content j_d_post_content
#class="p_author_name
from lxml import etree
import requests
import time
import json
from multiprocessing.dummy import Pool as ThreadPool
import sys
sys.getdefaultencoding()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

def towrite(contentdict):
    # f.writelines("回帖时间" + str(contentdict['topic_replay_time']) + '\n')
    f.writelines("回帖内容:" + str(contentdict['topic_reply_content']) + '\n')
    f.writelines("回帖人:" + str(contentdict['user_name']) + '\n')

def spider(url):
    # print("get----------------------------")
    print(url)
    html = requests.get(url,headers = headers)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class = "l_post l_post_bright j_l_post clearfix  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',""))
        author = reply_info['author']['user_name']
        if each.xpath('div[@class = "d_post_content_main "]/div/cc/div[@class = "d_post_content j_d_post_content "]/text()') != []:
            content = each.xpath('div[@class = "d_post_content_main "]/div/cc/div[@class = "d_post_content j_d_post_content "]/text()')[0]
        else:
            content = 'NULL'
        # reply_time = reply_info['content']['date']
        # print(content)
        # # print(reply_time)
        # print(author)
        item['user_name'] = author
        item['topic_reply_content'] = content
        # item['topic_reply_time'] = reply_time
        towrite(item)


if __name__ == '__main__':
    pool = ThreadPool(8)
    f = open('content.txt','a',encoding='utf-8')
    page = []
    for i in range(1,10):
        newpage = 'https://tieba.baidu.com/p/6117888348?pn=' + str(i)
        page.append(newpage)

    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()





























# html = requests.get("http://tu.duowan.com/tu",headers = headers)
# def getsource(url):
#     html = requests.get(url,headers = headers)
# urls = []
# for i in range(1,11):
#     newpage = 'https://tieba.baidu.com/p/6117888348?pn=' + str(i)
#     urls.append(newpage)
#
#
# print("多线程开始——————————————————")
# pool = ThreadPool(8)
# time3 = time.time()
# results = pool.map(getsource,urls)
# pool.close()
# pool.join()
# time4 = time.time()
# print("并行耗时：" + str(time4-time3))