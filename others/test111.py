import json

f = open("o.txt","r",encoding="utf-8")
w = open("user_json.json","w",encoding="utf-8")
content = f.read()
jj = json.loads(content)
print(jj)


