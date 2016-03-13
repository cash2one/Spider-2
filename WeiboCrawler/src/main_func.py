#coding:utf-8
import requests
from bs4 import BeautifulSoup
from weiboClass import Weibo
from userClass import User
from mytools.stringHandleByMyself import stripWithParamString

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

def UserCatchCore(headers,user_account_id,db):  
    userObj = User(user_account_id,headers)
    userObj.detailParseCoreRun()
    userObj.show_in_cmd()
    userObj.save_to_db(db)
    
def user_page_catch(fans_page_url,headers,db_user):
    response = requests.get(url=fans_page_url,headers=headers)
    soup = BeautifulSoup(response.text)
    table_list = soup.find_all('table')
    for user_info_table in table_list:
        a_list = user_info_table.find_all('a')
        user_homepage_url = a_list[0]['href']
        user_string = stripWithParamString(user_homepage_url,'http://weibo.cn/')
        if user_string[0]=='u':
            user_account_id = str(user_string[2:])
        else:
            response = requests.get(url=user_homepage_url,headers=headers)
            soup2 = BeautifulSoup(response.text)
            a_list = soup2.select('.ut')[0].find_all('a')
            for a in a_list:
                if a.text=='资料':
                    href = a['href']
                    user_account_id = href[1:-5]
                    break
        UserCatchCore(headers, user_account_id, db_user)
        print('----------------')