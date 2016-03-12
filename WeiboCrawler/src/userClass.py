#coding:utf-8
import requests,re
from bs4 import BeautifulSoup

class User(object):
    def __init__(self,user_account_id,headers,dbObj):
        self.userInfoLink =  'http://weibo.cn/' + user_account_id + '/info'
        self.database = dbObj
        self.account_id = user_account_id
        self.username = ''
        self.sex = 1
        self.area = ''
        self.authentication = ''
        self.birthday = ''
        self.abstract_info = ''
        self.tag = ''
        self.workExp = ''
        response = requests.get(url=self.userInfoLink,headers=headers)
        self.soup = BeautifulSoup(response.text)
    
    @property
    def head_pic_url(self):
        head_pic = self.soup.find('img')
        url = head_pic['src']
        return url
    
    def detailParseCoreRun(self):
        detail_list = self.soup.select('.c')
        match_string = detail_list[2].text
#         n = re.match(r'^([0-9a-zA-Z\_]{3})陆([0-9a-zA-Z\_]{3,8})$', match_string)
#         print(n)
#         print(n.groups())
#         m = re.match(r'^([\u4E00-\u9fa5]{3})-([\u4E00-\u9fa5]{3,8})$','陆你好-养你好葛琳')
#         print(m.groups())
#         >>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
#         >>> m
#         <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
#         >>> m.group(0)
#         '010-12345'
#         >>> m.group(1)
#         '010'
#         >>> m.group(2)
#         '12345'
        
    def save_to_db(self):
        pass