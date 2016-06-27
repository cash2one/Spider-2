#coding:utf-8
from mytools.stringHandleByMyself import stripWithParamString
import pymysql

class DoubanMovie250(object):
    '''
        This class is to catch douban.com movie's info
        and save them into mysql database. 
    '''
    def __init__(self,movie_li_html,dbObj):
        #bind method 
        self.database = dbObj
        self.movie_item = movie_li_html.select('.item')[0]
        self.main_role = ''
        self.birth = ''
        self.area = ''
        self.director = ''
        self.tag = ''
        #开局直接运行解析内核
        self.detailParseCoreRun()
    
    @property
    def rank(self):
        em_div = self.movie_item.find('em')
        num = int(em_div.text)
        return num
              
    @property
    def introduction_url(self):
        href_list = self.movie_item.select('a[href]')
        url = href_list[0]['href']
        return url
    
    @property
    def pic_src(self):
        pic_area = self.movie_item.select('.pic')[0]
        pic_src = pic_area.find('img')['src']
        return pic_src
        
    @property    
    def title(self):
        title_list = self.movie_item.select('.title')
        other_title_list = self.movie_item.select('.other')
        title_string = ''
        for t in title_list:
            title_string += t.text
        for t in other_title_list:
            title_string += t.text
        return title_string
    
    @property    
    def comment(self):
        try:
            comment_string = self.movie_item.select('.inq')[0].text
        except:
            comment_string = ''
        return comment_string
    
    @property    
    def score(self):
        score =  self.movie_item.select('.rating_num')[0].text
        return score
    
    def detailParseCoreRun(self):
        detail_string = self.movie_item.select('.bd')[0].find('p').text
        detail_list = detail_string.split('\xa0')
        info_list = []
        for item in detail_list:
            if item != '/' and item != '':
                info_list.append(item)
        director_string = info_list[0]
        director_string = stripWithParamString(director_string, '\n 导演：,,: ')
        self.director = director_string
        #处理主角以及年代
        t = info_list[1].split('\n')
        main_role_string = t[0]
        self.main_role = stripWithParamString(main_role_string,'主演: ')
        self.birth = t[1].strip(' ')
        #地区列表生成，首先去换行符
        area_list = info_list[2].split(' ')
        for area in area_list:
            if area:
                area = area.strip('\n')
                area += ','
                self.area += area
            else:
                break
        #标签列表生成，首先去换行符
        tag_list = info_list[3].split(' ')
        for tag in tag_list:
            if tag:
                tag = tag.strip('\n')
                tag += ','
                self.tag += tag
            else:
                break

    def show_info(self):
        #信息输出
        print('Rank:\t',self.rank)
        print('PicSrc:\t',self.pic_src)
        print('Title:\t',self.title)
        print('Introd_url:\t',self.introduction_url)
        print('Score:\t',self.score)
        print('Comment:\t',self.comment)
        print('Director:\t',self.director)
        print('MainRole:\t',self.main_role)
        print('Area:\t',self.area)
        print('Tag:\t',self.tag)
        print('Birth:\t',self.birth)
    
    def save_to_database(self):
        try:
            self.database.cur.execute("insert into movie(rank,picsrc,title,introduce_url,score,brief_comment,mainrole,area,tag,director,birth) " 
                                      "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.rank,self.pic_src,self.title,self.introduction_url,self.score,
                             self.comment,self.main_role,self.area,self.tag,self.director,self.birth))
            
            self.database.conn.commit()
            print('《',self.title,'》','更新成功')
        except pymysql.InternalError:
            pass
            
#         __author__ = 'luyang'
#         #导入pymysql的包
#         import pymysql
#         #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#         try:
#             conn=pymysql.connect(host='localhost',user='root',passwd='',db='doubanMovie',port=3306,charset='utf8')
#             cur=conn.cursor()#获取一个游标
#             cur.execute("insert into movie(rank,picsrc,title,introduce_url,score,brief_comment,mainrole,area,tag,director,birth)" 
#                             "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                         (self.rank,self.pic_src,self.title,self.introduction_url,self.score,
#                          self.comment,self.main_role,self.area,self.tag,self.director,self.birth)) 
#             conn.commit()
#             cur.execute('select * from movie')
#             data = cur.fetchall()
#             print(data)
#             print('《',self.title,'》','更新成功')
#         except  Exception :*+
#             print('《',self.title,'》','更新失败')
         
        

