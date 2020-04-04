import re
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
html = requests.get("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111",headers = headers)
# html.encoding = 'utf-8'
# html1 = re.findall('data-imgurl="(.*?)"/>',html,re.S)
print(html.text)
pic_url = re.findall('data-imgurl="(.*?)"',html.text,re.S)
i = 0
print(pic_url)
for each in pic_url:
    print('now downloading:' + i)
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i +=1
    if i > 40:
        break


