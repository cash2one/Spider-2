#codingL:utf-8

import pymysql
from commentClass import Comment
from userClass import User
import main_func

class Weibo(object):
    def __init__(self,weibo_div,headers,userDB,userID=''):
        self.userDB = userDB
        self.headers = headers
        self.weibo_div = weibo_div
        self.id = ''
        self.userID = userID
        self.origin_userID = ''
        self.content = ''
        self.create_time = ''
        self.flavor_cot = -1
        self.via_cot = -1
        self.comment_cot = -1
        self.platform = ''
        self.via_reason = ''
        self.topic = ''
        self.detail_parse_core()
    
    def create_comment(self,weiboID,authorID,content,db):
        commentObj = Comment(weiboID,authorID,content)
        commentObj.save_to_database(db)
    
    def create_user(self,user_account_id,headers,db):
        userObj = User(user_account_id,self.headers)
        userObj.save_to_db(db)

    def create_topic(self):
        pass
        
    def detail_parse_core(self):
        self.id = self.weibo_div['id']
        author_area = self.weibo_div.select('.nk')
        if author_area!=[]:
            user_homepage_url = author_area[0]['href']
            print('input:',user_homepage_url)
            self.userID = main_func.GetUserAccountID(user_homepage_url,self.headers)
        self.content = self.weibo_div.select('.ctt')[0].text
        via_list = self.weibo_div.select('.cmt')
        if len(via_list)==4:
            #此情况适用于转发的微博
#             origin_user_homepage_url = via_list[0].select('a')[0]['href']
#             origin_userID = main_func.GetUserAccountID(origin_user_homepage_url,self.headers)
#             main_func.UserCatchCore(self.headers, origin_userID, self.userDB)
            #ct_class = self.weibo_div.select('.ct')
            last_div = self.weibo_div.contents[-1]
            detail_list = last_div.contents[1:]
            info_list = []
            for info in detail_list:
                if info !='\xa0\xa0' and info!='\xa0' and info!=' ':
                    info_list.append(info)
            #得到转发理由字符串        
            via_reason_list = info_list[:-5]
            via_reason_string = ''
            print(via_reason_list)
            for info in via_reason_list:
                try:
                    info['href']
                    info = info.text
                except:
                    pass
                via_reason_string += info
            self.via_reason = via_reason_string
            #得到点赞转发评论数（非原文）
            cot_list = info_list[-5:]
            def get_flavor_cot(self):
                pass
            def get_via_cot(self):
                pass
            def get_comment_cot(self):
                pass
            def get_create_time(self):
                pass
            def get_resource_and_resource(self):
                pass
            def void_func(self):
                pass
            
#             dict={
#                   u'赞':  get_flavor_cot,
#                   u'转':  get_via_cot,
#                   u'评':  get_comment_cot,
#                   u'收':  void_func,
#                   u'今':  get_resource_and_resource,
#                   }
            for info in cot_list:
                print(info.text)
                j = info.text.encode('utf-8')
                print(j)
                for x in j:
                    print(x)
                #print(str(info.text)[0])
                
                #print(type(i))
#                 via_reason += 
                
#             div = ct_class.parent
#             print(div)
#             print(type(div))
        print('------------')
        
    def save_to_db(self,db):
        pass
        