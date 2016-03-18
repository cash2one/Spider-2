#coding:utf-8

import pymysql,time
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
        if userID != '':
            res = userDB.isExist('user','account_id',userID)
            if not res:
                print('sb')
                main_func.UserCatchCore(headers,userID,userDB)
        self.origin_userID = ''
        self.content = ''
        self.create_time = ''
        self.flavor_cot = -1
        self.via_cot = -1
        self.comment_cot = -1
        self.platform = ''
        self.via_reason = ''
        self.detail_parse_core()
    
    def show_in_cmd(self):
        print('++++++++++++++微博信息+++++++++++++')
        print('id:\t\t\t',self.id)
        print('userID:\t\t\t',self.userID)
        print('origin_userID:\t\t',self.origin_userID)
        print('via_reason:\t\t',self.via_reason)
        print('content:\t\t',self.content)
        print('create_time:\t\t',self.create_time)
        print('flavor_cot:\t\t',self.flavor_cot)
        print('via_cot:\t\t',self.via_cot)
        print('comment_cot:\t\t',self.comment_cot)
        print('platform:\t\t',self.platform)
        print('++++++++++++++微博信息+++++++++++++')
        
        
    def create_comment(self,weiboID,authorID,content,db):
        commentObj = Comment(weiboID,authorID,content)
        commentObj.save_to_database(db)
    
    def create_user(self,user_account_id,headers,db):
        userObj = User(user_account_id,self.headers)
        userObj.save_to_db(db)
        
    def detail_parse_core(self):
        try:
            self.id = self.weibo_div['id']
        except:
            print(self.weibo_div)
        author_area = self.weibo_div.select('.nk')
        if author_area!=[]:
            #等于[]时表明在探测某人主页
            user_homepage_url = author_area[0]['href']
            self.userID = main_func.GetUserAccountID(user_homepage_url,self.headers)
        self.content = self.weibo_div.select('.ctt')[0].text
        #-------------------------
        last_div = self.weibo_div.contents[-1]
        detail_list = last_div.contents[1:]
        info_list = []
        for info in detail_list:
            if info !='\xa0\xa0' and info!='\xa0' and info!=' ':
                info_list.append(info)
        #得到点赞转发评论数（非原文）
        cot_list = info_list[-5:]
        #print(cot_list)
        def get_flavor_cot(string):
            self.flavor_cot = int(string[2])
        def get_via_cot(string):
            self.via_cot = int(string[3])
        def get_comment_cot(string):
            self.comment_cot = int(string[3])
        def void_func(string):
            pass
        def get_resource_and_time(string):
            str_list = string.split('\xa0')
            self.platform = str_list[1][2:]
            #发表时间以后修改 不要忘记！！！！！！！！
             
        dict = {
                  '赞':  get_flavor_cot,
                  '转':  get_via_cot,
                  '评':  get_comment_cot,
                  '收':  void_func,
              }
        for info in cot_list[:-1]:
            detail = info.text
            key = detail[0]
            func = dict[key]
            func(detail)
         
        last_info = cot_list[-1].text
        get_resource_and_time(last_info)
        #---------------------------------------------
        via_list = self.weibo_div.select('.cmt')
        self.origin_userID = self.userID
        if len(via_list)==4:
            #此情况适用于转发的微博
            origin_user_homepage_url = via_list[0].select('a')[0]['href']
            origin_userID = main_func.GetUserAccountID(origin_user_homepage_url,self.headers)
            print("\n原创用户搜索中")
            main_func.UserCatchCore(self.headers, origin_userID, self.userDB)
            self.origin_userID = origin_userID
            
            #得到转发理由字符串        
            via_reason_list = info_list[:-5]
            via_reason_string = ''
            for info in via_reason_list:
                try:
                    info['href']
                    info = info.text
                except:
                    pass
                via_reason_string += info
            self.via_reason = via_reason_string
            
        print('------------')
        
    def save_to_db(self,db):
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        try:
            db.cur.execute(
                "insert into weibos(create_time,id,userID,content,flavor_cot,via_cot,comment_cot,origin_userID,via_reason,platform)"
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (now,self.id,self.userID,self.content,self.flavor_cot,self.via_cot,self.comment_cot,self.origin_userID,self.via_reason,self.platform)
            )
            db.conn.commit()
            self.show_in_cmd()
            print('save weibos successfully')
        except pymysql.InternalError:
            pass
        