import requests
import re
import sys
import importlib as imp
imp.reload(sys)

class spider(object):
    def __init__(self):
        print("开始爬取内容___")
    def getsource(self,url):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        html = requests.get(url,headers = header)
        html.encoding = 'utf-8'
        return html.text
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group
    def geteveryclass(self,source):
        everyclass = re.findall('<li id=.*?</li>',source,re.S)
        return everyclass
    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('title="(.*?)"',eachclass,re.S).group(1)
        info['content'] = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['classtime'] = timeandlevel[0]
        info['level'] = timeandlevel[1]
        info['learnnum'] = re.search('<em class="learn-number">(.*?)</em>',eachclass,re.S).group(1)
        return info

    def saveinfo(self,classinfo):
        with open('info.txt','a') as f:
            i = 0
            for each in classinfo:
                f.writelines('title:' + "".join(each['title'].split()) + '\n')
                f.writelines('content:' + "".join(each['content'].split()) + '\n')
                f.writelines('classtime:' + "".join(each['classtime'].split()) + '\n')
                f.writelines('level:' + "".join(each['level'].split()) + '\n')
                f.writelines('learnnum:' + "".join(each['learnnum'].split()) + '\n')
                f.writelines('\n')
                f.writelines('第%s个'%i + '\n')
                i += 1

if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url,20)
    for link in all_links:
        print('正在处理页面： ' + link)
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)