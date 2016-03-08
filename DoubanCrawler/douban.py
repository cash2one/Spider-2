#coding:utf-8
import requests
from bs4 import BeautifulSoup
from stringHandleByMyself import stripWithParamString

class DoubanMovie250(object):
    def __init__(self,movie_li_html):
        self.movie_item = movie_li_html.select('.item')[0]
        self.main_role = ''
        self.birth = ''
        self.area_list = []
        self.director = ''
        self.tag_list = []
        #开局直接运行解析内核
        self.detailParseCoreRun()
          
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
        comment = self.movie_item.select('.inq')[0].text
        return comment
    
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
                self.area_list.append(area)
            else:
                break
        #标签列表生成，首先去换行符
        tag_list = info_list[3].split(' ')
        for tag in tag_list:
            if tag:
                tag = tag.strip('\n')
                self.tag_list.append(tag)
            else:
                break

    def show_info(self):
        #信息输出
        print('PicSrc:\t',movieObj.pic_src)
        print('Title:\t',movieObj.title)
        print('Introd_url:\t',movieObj.introduction_url)
        print('Score:\t',movieObj.score)
        print('Comment:\t',movieObj.comment)
        print('Director:\t',movieObj.director)
        print('MainRole:\t',movieObj.main_role)
        print('Area_list:\t',movieObj.area_list)
        print('Tag_list:\t',movieObj.tag_list)
        print('Birth:\t',movieObj.birth)
    
    def save_to_database(self):
        pass
    
    
    
if __name__ == '__main__':
    headers = {
       'cookie':'bid="H/8WtiieLZY"; ll="118161"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1457329425%2C%22http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dqfn06gOhi-wtrX-NVr6bDgb-ErDBNZyr-BGwOVqjEha%26wd%3D%26eqid%3D9a205b46000e49050000000356dd1512%22%5D; _pk_id.100001.8cb4=ad8c39800b28e039.1457281628.2.1457329507.1457281658.; __utma=30149280.301580234.1457281632.1457281632.1457329434.2; __utmz=30149280.1457329434.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; _pk_ses.100001.8cb4=*; __utmb=30149280.3.10.1457329434; __utmc=30149280; __utmt=1; dbcl2="142895985:ql5M3jojOVc"; ck="BRZz"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14289',
       'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
    
    url = 'https://movie.douban.com/top250'
    
    response = requests.get(url,headers=headers)
    
    soup = BeautifulSoup(response.text)
    
    mainarea = soup.select('.grid_view')[0]
    
    cot = 0
    
    for movie in mainarea:
        cot += 1
        if cot % 2 == 0:
            movieObj = DoubanMovie250(movie)
            movieObj.show_info() 
            print("----------------------")
        
    print(cot)
