import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# html = requests.get("http://tu.duowan.com/tu",headers = headers)
def getsource(url):
    html = requests.get(url,headers = headers)
urls = []
for i in range(1,21):
    newpage = 'http://www.jikexueyuan.com/course/?pageNum=' + str(i)
    urls.append(newpage)


print("单线程开始————————————————")
time1 = time.time()
for url in urls:
    getsource(url)
time2 = time.time()
print("单线程耗时：" + str(time2-time1))

print("多线程开始——————————————————")
pool = ThreadPool(8)
time3 = time.time()
results = pool.map(getsource,urls)
pool.close()
pool.join()
time4 = time.time()
print("并行耗时：" + str(time4-time3))