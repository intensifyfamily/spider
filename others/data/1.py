# import json
# f = open("test2.html", "r", encoding='utf-8')
# res = f.read()
# oo = json.loads(res)
# print(oo)

import os

fileObject = file("D:/text.txt", "a+")  # 以追加的方式
fileObject.seek(-1, os.SEEK_END)
fileObject.truncate()
fileObject.close()