#coding:utf-8
import requests
from bs4 import BeautifulSoup
from weiboClass import Weibo
from userClass import User

def catch_weibo_info(headers,entrance_url,db):
    response = requests.get(utl=entrance_url,headers=headers)
    soup = BeautifulSoup(response.text)
    weibo_list_area = soup.select('.c')
    weibo_list_area = weibo_list_area[1:-2]
    for weibo in weibo_list_area:
        id = weibo['id']
        author = weibo.a.text
        print(weibo)
        weiboObj = Weibo(db)
        pass
    pass

def catch_user_info(headers,user_account_id,db):
    userObj = User(user_account_id,headers,db)
    #userObj.detailParseCoreRun()
    userObj.save_to_db()