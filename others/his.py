import requests
import pymysql
from bs4 import BeautifulSoup
import numpy as py
import pandas as pd

con=pymysql.connect('localhost','root','root','pythonDB')
url ="https://xiaoyuan.zhaopin.com/part/0/0_0_0_0_0_-1_人工智能_{}_0"

f= requests.get(url.format(1)).text
soup = BeautifulSoup(f, "html.parser")
page= soup.find("span",attrs={"class":"searchResultPagePer fr"}).get_text()
db=con.cursor()


time=page[2:4]
#time=page.split("/")[1]
with open("infomation.csv","a+",encoding="utf-8") as q:
    q.write('job#num#jobtype#city#company#pubtime')
    for i in range(1,int(time)+1):
        f=requests.get(url.format(i)).text
        soup=BeautifulSoup(f,"html.parser")
        divlist=soup.find_all(class_="searchResultItemSimple clearfix")

        for div in divlist:
            job = div.find\
                ("a").get_text()
            city=div.find("em",attrs={"class":"searchResultJobCityval"}).get_text()
            num=div.find("em",attrs={"class":"searchResultJobPeopnum"}).get_text()
            jobtype=div.find("p",attrs={"class":"searchResultCompanyIndustry"}).get_text()
            company=div.find("p",attrs={"class":"searchResultCompanyname"}).get_text()
            pubtimezzz=div.find("p",attrs={"class":"pt15 pb10"})
            pubtimezz=pubtimezzz.find("span")
            pubtimez=pubtimezz.find("span").get_text()
            pubtime=pubtimez[7:]
            #note=div.find("span",attrs={"class":"oTips oTips1 fl"}).get_text()
            sql = "insert into jobinfo(jobname,neednum,jobtype,city,company,pubtime) values ('{}','{}','{}','{}','{}','{}')".format(job,num,jobtype,city,company,pubtime)
            db.execute(sql)
            con.commit()
            q.write('{}#{}#{}#{}#{}#{}'.format(job,num,jobtype,city,company,pubtime)+'\n')
            print("sql结束")

db.close()
con.close()
print("爬虫结束")