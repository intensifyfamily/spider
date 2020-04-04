import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
html = requests.get("https://tieba.baidu.com/f?kw=%C8%D5%B1%BE%C2%FE%BB%AD&fr=ala0&tpl=5&traceid=",headers = headers)
html.encoding = 'utf-8'
# print(html.text)
titles = re.findall('target="_blank" class="j_th_tit ">(.*?)</a>',html.text,re.S)
for each in titles:
    print(each)



