import socket
import re
from time import sleep
import datetime
import json
import requests
#import pycryptodome
#import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

socket.gethostname() #获取当前主机名

#通过hostname查询,注意这个并不一定会得到真确的IP地址

print(socket.gethostbyname(socket.gethostname()))

#通过访问自己UDP方式获取，这个会获取当前的准确地址

def get_host_ip():

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(('8.8.8.8', 80))

        ip = s.getsockname()[0]

    finally:

        s.close()

    return ip

print(get_host_ip())

#获取所有IP地址

addrs = socket.getaddrinfo(socket.gethostname(),None)  #获取当前主机的所有ip地址





#企业微信推送

def QwxPush(Qwx_message):

    corpid='ww40a44ba4adad3a31'

    corpsecret='VCPhlNwx5tJq6pi_Wv8iG6aPdXdZns1xK39DyP8Z7Rg'

    agentid=1000002

    access_token_url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'

    reg = requests.get(url=access_token_url)

    access_token=json.loads(reg.text)['access_token']

    #print(reg.text)

    send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'

    #message='hello!'

    send_msg = {

                "touser": "@all",

                "msgtype": "text",

                "agentid": agentid,

                "text": {

                    "content": Qwx_message,

                },

            }

    requests.post(url=send_msg_url, data=json.dumps(send_msg))

'''


for item in addrs:

    print(item)
    QwxPush(item)
