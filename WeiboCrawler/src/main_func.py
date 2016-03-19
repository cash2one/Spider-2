#coding:utf-8
import requests,time
from bs4 import BeautifulSoup
from weiboClass import Weibo
from userClass import User
from mytools.stringHandleByMyself import stripWithParamString
from mytools.emailClass import Email

def CrawlSpecificUserWeibosInfo(userID,headers,db):
    res = db.isExist('user','account_id',userID)
    if not res:
        UserCatchCore(headers,userID,db)
    profile_url = 'http://weibo.cn/'+ userID +'/profile'
    response = requests.get(url=profile_url,headers=headers)
    soup = BeautifulSoup(response.text)
    weibo_list_area = soup.select('.c')
    weibo_list_area = weibo_list_area[:-2]
    length = len(weibo_list_area)
    print('list length = ', length)
    print(response)
    status = 0
    if length is 0:
        print(response)
    if length is 14:
        #被恶意指向微博广场
        return 2
    if length<10 and length>1:
        print('此人微博少于十条')
        status = 3
    for weibo_div in weibo_list_area:
        weiboObj = Weibo(weibo_div,headers,db,userID)
        try:
            weiboObj.save_to_db(db)
            status = 1
        except Exception as e:
            print(e)
    return status    
    
def CrawlMyFocusWeibo(headers,db):
    url = 'http://weibo.cn/?tf=5_009&vt=4'
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text)
    weibo_list_area = soup.select('.c')
    weibo_list_area = weibo_list_area[:-2]
    print('list length = ', len(weibo_list_area))
    for weibo_div in weibo_list_area:
        weiboObj = Weibo(weibo_div,headers,db)
        weiboObj.save_to_db(db)
    
def UserCatchCore(headers,user_account_id,db):
    data = db.getData('user','account_id')
    for item in data:
        if item==user_account_id:
            print('该用户已经存过')
            return
    userObj = User(user_account_id,headers)
    if (userObj.fans_cot<10 and userObj.weibo_cot<10):
        RemoveFans(user_account_id, headers)
        print(userObj.username,'已清理')
        print('fans:',userObj.fans_cot)
        print('weibo:',userObj.weibo_cot)
        print('foucs:',userObj.focus_cot)
        return
    userObj.save_to_db(db)
    
def GetUserAccountID(user_homepage_url,headers):
    '''
    user_homepage_url format as:
    1.http://weibo.cn/leimingz
    2.http://weibo.cn/u/1742566624
    3.http://weibo.cn/leimingz?vt=4
    4.http://weibo.cn/u/1742566624?vt=4
    '''
    end = user_homepage_url[-5:]
    if end=='?vt=4':
        user_homepage_url = user_homepage_url[:-5]
    user_account_id = ''
    user_string = stripWithParamString(user_homepage_url,'http://weibo.cn/')
    if user_string[0]=='u' and user_string[2]=='u' and user_string[1]=='/':
        user_account_id = str(user_string[2:])
    else:
        response = requests.get(url=user_homepage_url,headers=headers)
        soup2 = BeautifulSoup(response.text)
        try:
            a_list = soup2.select('.ut')[0].find_all('a')
        except:
            return user_account_id
        for a in a_list:
            if a.text=='资料':
                href = a['href']
                user_account_id = href[1:-5]
                break
    return user_account_id

def fans_page_catch(fans_page_url,headers,db_user):
    response = requests.get(url=fans_page_url,headers=headers)
    soup = BeautifulSoup(response.text)
    try:
        table_list = soup.find_all('table')
        for fans_info_table in table_list:
            a_list = fans_info_table.find_all('a')
            fans_homepage_url = a_list[0]['href']
            fans_account_id = GetUserAccountID(fans_homepage_url,headers)
            UserCatchCore(headers, fans_account_id, db_user)
            print('----------------')
    except Exception as err:
        print(soup)
        print(err)
        
def CrawlSpecificUserFansInfo(userID,headers,db,start=0,end=100):
    start_page_url = 'http://weibo.cn/'+ userID +'s'
    cot = start 
    while cot<end+1:
        print('Page------',cot)
        fans_page_url = start_page_url + '?&page=' + str(cot)
        print(fans_page_url)
        fans_page_catch(fans_page_url,headers,db)
        cot += 1

def RemoveFans(fansID,headers):
    removeUrl = 'http://weibo.cn/attention/remove?act=removec&uid='+ fansID +'&rl=1&st=0e83c9'
    requests.get(url=removeUrl,headers=headers)
    
def send_email(author,content):
    local_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    receiver = '2733641279@qq.com'  
    sender = '15262057539@163.com'    
    subject = '惠普捕获到【'+ author + '】的微博了！快去看看吧！' + local_time
    host = 'smtp.163.com'  
    port = 25
    username = '15262057539@163.com'  
    password = 'luyang716'   
    print('content:',content)
    emailObj = Email(sender,receiver,subject,content)
    emailObj.conn_server(host,port)
    emailObj.login(username, password)
    emailObj.send()
    emailObj.close()
