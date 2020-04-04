# from lxml import etree
import requests
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
html = requests.get("https://www.zhihu.com/people/jeffreycheung",headers = headers)

selector = etree.HTML(html.text)
content_field = selector.xpath('//script[@id = "js-initialData"]/text()')[0]
print(content_field)

































# html = '''<html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>demo</title>
# </head>
# <body>
# <div id="test-1">需要得内容1</div>
# <div id="test-2">需要得内容2</div>
# <div id="test-3">需要得内容3</div>
# <div id="testfault">需要得内容4</div>
# </body>
# </html>'''
#
# html2 = '''<html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>demo</title>
# </head>
# <body>
# <div id="test-1">左青龙
# <span id = 'tiger'>右白虎</span>
# <ul>中间一个
# <li>二百五</li></ul>
# </div>'''

#xpath

# selector = etree.HTML(html)
# content = selector.xpath('//img/@src')
# for each in content:
#     # with open('tree.txt','w',encoding='utf-8') as f:
#     #     f.writelines(str(each))
#     print(each)



# (starts-with)

# selector = etree.HTML(html)
# content = selector.xpath('//div[starts-with(@id,"test")]/text()')
# for each in content:
#     print(each)


#string(.)

# selector = etree.HTML(html2)
# content = selector.xpath('//div[@id="test-1"]')[0]
# info = content.xpath('string(.)')
# content2 = info.replace('\n','').replace(' ','')
# print (content2)