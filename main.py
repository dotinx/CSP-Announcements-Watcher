from time import sleep
import requests
import datetime
import time
from bs4 import BeautifulSoup
import os
urlbase = "https://cspsj.noi.cn/page/index/noiNews.php?id="
index = 59
let = ""
while True:
    req_time = datetime.datetime.now()
    res = requests.get(urlbase+str(index))
    soup = BeautifulSoup(res.text,"lxml")
    et = soup.find("div","panel-body")
    if et != let:
        print("\n")
        let = et
        print(et)
        print("\n\r已更新 ",req_time.strftime("%Y-%m-%d %H:%M:%S"),end="")
        os.system("hh "+"http://cspsj.noi.cn/page/index/noiNews.php?id="+str(index))
    else:
        print("\r未更改 ",req_time.strftime("%Y-%m-%d %H:%M:%S"),end="")
    sleep(5)