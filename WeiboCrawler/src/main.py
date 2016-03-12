#coding:utf-8

from mytools.MyDatabaseClass import MyDatabase
from main_func import catch_user_info,catch_weibo_info
import requests
from bs4 import BeautifulSoup
from mytools.stringHandleByMyself import stripWithParamString
from userClass import User

if __name__ == '__main__':
    headers = {
       'cookie':'SUB=_2A25758zaDeRxGeRI4lMT9i7Pwz-IHXVZK9SSrDV6PUJbstANLUXdkW1LHetM10ibDtTzXbOjGUpSspPbu0hF0g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWmV6.d3FPdoC6bsHYoP.uo5JpX5o2p; SUHB=0S7DerNYZ4Yole; SSOLoginState=1457765514',
       'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
    weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')
    
#     url = 'http://weibo.cn/'
#     
#     catch_weibo_info(headers, url, weiboDB)

    fans_page_url = 'http://weibo.cn/2691260383/fans'
    '''
            以id为2691260383账号为树的根节点遍历
    '''
    
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
        print(user_account_id)
        userInfoLink =  'http://weibo.cn/' + user_account_id + '/info'    
        print(userInfoLink) 
        #catch_user_info(headers, user_account_id, weiboDB)
        userObj = User(user_account_id,headers,weiboDB)
        userObj.detailParseCoreRun()
        print('----------------')