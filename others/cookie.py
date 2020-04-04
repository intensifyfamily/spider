import requests
from lxml import etree

cook = {'Cookie': "SCF=AsROq-pRVPPBuYI-IXprAaRvYfb5QlKSEaQR_QVW5hjD-Pf7QEKWyOyojgCNcQYfRTIO8NkH6LtKkFAxsGBlXFs.; SUHB=0BLoTYM5HMJsnD; _T_WM=10429642964; SUB=_2A25x3x7rDeRhGeNM6VoY-SrMyTiIHXVTI6KjrDV6PUJbkdAKLUXMkW1NTiVT-J7gTpw5yrhch-8A5JvsQPCkTfpe"}
url = "https://weibo.cn/cyez"
# # html = requests.get(url).content
# # print(html)




html = requests.get(url,cookies = cook).content#如果这里用text
#html = bytes(bytearray(html, encoding='utf-8'))
selector = etree.HTML(html)
content = selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print(text)
