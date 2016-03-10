#coding:utf-8
import requests
from bs4 import BeautifulSoup
from doubanClass import DoubanMovie250

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
            #movieObj.show_info() 
            movieObj.save_to_database()
            print("----------------------")
        
    print(cot)
