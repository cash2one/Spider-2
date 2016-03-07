#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup

class DoubanMovie250(object):
    def __init__(self,movie_li_html):
        self.movie_item = movie_li_html.select('.item')[0]
        self.main_role = ''
        self.birth = ''
        self.country = ''
        self.director = ''
        self.tag = ''
        
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
    
    @property  
    def detail(self):
        detail_string = self.movie_item.select('.bd')[0].find('p').text
        return detail_string
    
    def info_RegularExpression_insolver(self):
        detail = self.detail
        pattern_cailiao=re.compile(r"(%s.*?|%s.*?|%s.*?)"%(cailiao1,cailiao2,cailiao3),re.S)
        for match in re.finditer(pattern_cailiao,detail):
            cailiao=match.group(1)
            file1.write(cailiao)
            file1.write("\n")
        
    
    
    
    
headers = {
   'cookie':'bid="H/8WtiieLZY"; ll="118161"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1457329425%2C%22http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dqfn06gOhi-wtrX-NVr6bDgb-ErDBNZyr-BGwOVqjEha%26wd%3D%26eqid%3D9a205b46000e49050000000356dd1512%22%5D; _pk_id.100001.8cb4=ad8c39800b28e039.1457281628.2.1457329507.1457281658.; __utma=30149280.301580234.1457281632.1457281632.1457329434.2; __utmz=30149280.1457329434.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; _pk_ses.100001.8cb4=*; __utmb=30149280.3.10.1457329434; __utmc=30149280; __utmt=1; dbcl2="142895985:ql5M3jojOVc"; ck="BRZz"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.14289',
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
   }

url = 'https://movie.douban.com/top250'

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text)
mainarea = soup.select('.grid_view')[0]

# print(type(mainarea))
# print(mainarea)

cot = 0
for movie in mainarea:
    cot += 1
    if cot % 2 == 0:
#         movie_item = movie.select('.item')[0]
#         pic_area = movie_item.select('.pic')[0]
#         pic_src = pic_area.find('img')['src']
#         print(pic_src)

        movieObj = DoubanMovie250(movie)
        print(movieObj.pic_src)
        print(movieObj.title)
        print(movieObj.introduction_url)
        print(movieObj.score)
        print(movieObj.comment)
        movieObj.detail()
        print("----------------------")
    
print(cot)
