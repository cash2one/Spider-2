#coding:utf-8
import requests
from bs4 import BeautifulSoup
from weiboClass import Weibo
from userClass import User
from mytools.stringHandleByMyself import stripWithParamString

def CrawlSpecificUserWeibosInfo(userID,headers,db):
#     response = requests.get(url=entrance_url,headers=headers)
#     soup = BeautifulSoup(response.text)
#     weibo_list_area = soup.select('.c')
#     weibo_list_area = weibo_list_area[1:-2]
#     for weibo in weibo_list_area:
#         id = weibo['id']
#         author = weibo.a.text
#         print(weibo)
#         weiboObj = Weibo(db)
#         pass
    pass

def UserCatchCore(headers,user_account_id,db):
    data = db.getData('user')
    for item in data:
        if item[0]==user_account_id:
            print('该数据已经存过')
            return
    userObj = User(user_account_id,headers)
    userObj.homepageParseCoreRun()
    if (userObj.fans_cot<10 and userObj.weibo_cot<10) or userObj.focus_cot>1500:
        RemoveFans(user_account_id, headers)
        print(userObj.account_id,'已清理')
        print('fans:',userObj.fans_cot)
        print('weibo:',userObj.weibo_cot)
        print('foucs:',userObj.focus_cot)
        return
    userObj.detailParseCoreRun()
    userObj.show_in_cmd()
    if userObj.weibo_cot != 888888:
        userObj.save_to_db(db)
    
def GetUserAccountID(user_homepage_url,headers):
    user_account_id = ''
    user_string = stripWithParamString(user_homepage_url,'http://weibo.cn/')
    if user_string[0]=='u' and user_string[1]=='/':
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
    return user_account_id

def fans_page_catch(fans_page_url,headers,db_user):
    response = requests.get(url=fans_page_url,headers=headers)
    soup = BeautifulSoup(response.text)
    table_list = soup.find_all('table')
    for fans_info_table in table_list:
        a_list = fans_info_table.find_all('a')
        fans_homepage_url = a_list[0]['href']
        fans_account_id = GetUserAccountID(fans_homepage_url,headers)
        UserCatchCore(headers, fans_account_id, db_user)
        print('----------------')
        
def CrawlSpecificUserFansInfo(userID,headers,db,start):
    start_page_url = 'http://weibo.cn/'+ userID +'/fans'
    cot = start
    while cot<101:
        print('Page------',cot)
        fans_page_url = start_page_url + '?&page=' + str(cot)
        print(fans_page_url)
        fans_page_catch(fans_page_url,headers,db)
        cot += 1
        if cot==101:
            cot = 20

def RemoveFans(fansID,headers):
    removeUrl = 'http://weibo.cn/attention/remove?act=removec&uid='+ fansID +'&rl=1&st=0e83c9'
    response = requests.get(url=removeUrl,headers=headers)