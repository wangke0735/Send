import requests
import time
import random
import datetime
import json
import os
import threading
import sys
import os, re
import hmac
import hashlib
import base64
import urllib.parse
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from datetime import datetime


def env(key):
    return os.environ.get(key)



if env("CFD_NUM"):
    
    num=(env("CFD_NUM").split('&'))[0]
else:
    num=0






try:
    from sendNotify import send
    print('加载了senNotify')
except:
    try:
        from notify import send
        print('加载了notify')
    except:
        print('找不到通知文件，没有通知')
        send=None



cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)



try:
    from ping3 import ping
except ImportError:
    print("正在导入ping3模块")
    os.system("pip install ping3")
    os.system("pip3 install ping3")




if env("JD_COOKIE"):
    
    cookies=(env("JD_COOKIE").split('&'))
   
print('默认第一个，脚本中18行修改num变量选择ck，完整ck列表：')
print(cookies)
print('****************************************************') 
print('当前使用ck为:'+cookies[num])




headers={"Host":"m.jingxi.com",
                    "Accept":"*/*",
                    "Accept-Encoding":"gzip, deflate, br",
                    "User-Agent":"jdpingou;iPhone;5.11.0;15.1;4305736ed7317d2e8cbbcd0959427edb8d84a4c8;network/wifi;model/iPhone12,1;appBuild/100755;ADID/;supportApplePay/1;hasUPPay/0;pushNoticeIsOpen/0;hasOCPay/0;supportBestPay/0;session/86;pap/JA2019_3111789;brand/apple;supportJDSHWK/1;Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
                    "Accept-Language":"zh-CN,zh-Hans;q=0.9",
                    "Referer":"https://st.jingxi.com/",
                    "Cookie":cookies[num]}
def req(url,headers):
    response=requests.get(url,headers=headers)
    print(response.text)
    return response.text

def yfc():
    i=1
    response=str(random.uniform(1, 10))#每次通知不一样，防止不通知
    time_ys=(ping("m.jingxi.com"))/2
    print(time_ys)

    
    if env("CFD_HB"):
    
        url=(env("CFD_HB").split('&'))[0]
    else:
        url="https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7&_cfd_t=1638174242869&ptag=7155.9.47&dwType=3&dwLvl=13&ddwPaperMoney=100000&strPoolName=jxcfd2_exchange_hb_202111&strPgtimestamp=1638174242867&strPhoneID=e0d77f0905bffb0ef35ed5e108e1d96d88115814&strPgUUNum=e8fde476fcea928b19c7af6cfa854221&_stk=_cfd_t%2CbizCode%2CddwPaperMoney%2CdwEnv%2CdwLvl%2CdwType%2Cptag%2Csource%2CstrPgUUNum%2CstrPgtimestamp%2CstrPhoneID%2CstrPoolName%2CstrZone&_ste=1&h5st=20211129162402869%3B6326065138416163%3B10032%3Btk01w63111ad930nNvGBh232LFXKzS7b8Yi73yW4Wb8yles41Q9adMg%2FRMC7d8MANxBFSUp9iRoPeMW9aDnFYAp3rzVF%3B165923ce5dd325386b78769ecde423502d01c18fef4eb6ddc2f966d4682fa4c6&_=1638174242870&sceneval=2&g_login_type=1&callback=jsonpCBKR&g_ty=ls"


   
    time_fb=3600-(time.time()+time_ys)%3600
    print('延迟{}后执行'.format(time_fb))
    time.sleep(time_fb-0.003)
    print(time_fb)

    while(i<4):

        print('正在发包，第%d次'%(i))
        print((time.time()+time_ys)%3600)
        com=str(req(url,headers))                   
        print(str(com))
        response+=str(com)                
        i+=1
        time.sleep(0.3)
    
           



   
    send('财富岛抢购通知',response)

yfc()
sys.exit()
