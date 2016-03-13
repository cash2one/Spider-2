#coding:utf-8

from mytools.MyDatabaseClass import MyDatabase
from main_func import user_page_catch

if __name__ == '__main__':
    headers = {
               'cookie':'SUHB=0z1B1fhZjG7DCe; _T_WM=bef2c515f1bcb67425331213a5262a1b; SUB=_2A2574RbNDeRxGeRI4lMT9i7Pwz-IHXVZLbqFrDV6PUJbrdANLRH6kW1LHetxlcUhmY6ME57DOcClitlj_c9o_w..; M_WEIBOCN_PARAMS=from%3Dhome; gsid_CTandWM=4uINa35c1jX4SthOuMlNCbi7q6b',
              'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
    weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')
    
#     url = 'http://weibo.cn/'
#     
#     catch_weibo_info(headers, url, weiboDB)

    start_page_url = 'http://weibo.cn/2691260383/fans'
    '''
            以id为2691260383账号为树的根节点遍历
    '''
    cot = 1
    while cot<100:
        fans_page_url = start_page_url + '?&page=' + str(cot)
        print(fans_page_url)
        cot += 1
        user_page_catch(fans_page_url,headers,weiboDB)