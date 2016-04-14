# coding=utf-8

#import psycopg2
import requests
from bs4 import BeautifulSoup

class IEEE_Artile(object):
    def __init__(self,article_div):
        #根据每个文章所属li标签建类，而非目录页面的url
        self.txt = article_div.select('.txt')[0]
        self.control = article_div.select('.controls')[0]
        self.pdf_url = ''
        self.html_url = ''
        self.pdf_html_url()
    
    def pdf_html_url(self):
        for i in self.control.select('a[href]'):
            href = i['href']
            if href != '#':
                if href.startswith('/stamp'):
                    self.pdf_url = href
                elif href.startswith('/xpls'):
                    self.html_url = href
                else:
                    pass
    
    def save_to_database(self):
        #！！！！！新添加的keywords需要进行Update
        try:
            conn = psycopg2.connect("dbname=essays user=gao password={}".\
                format(os.environ.get('pg_password')))
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute(
                "insert into ieee (title, authors, abstract, pdf_url, html_url)"
                "values (%s, %s, %s, %s, %s)", 
                (self.title, self.author, self.abstract, self.pdf_url, self.html_url)
            )
            cur.close()
            conn.close()
        except Exception as err:
            print(err)
        return
                
    def show_in_cmd(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Abstract:",self.abstract_info)
        print("Keywords:",self.keywords)
    
    @property
    def title(self):
        span = self.txt.find('span')
        title = span.text
        return title
    
    @property
    def author(self):
        authors = self.txt.select('.authors')[0]
        name_area = authors.select('.authorPreferredName')
        name_list = []
        for name in name_area:
            name =  name.select('#preferredName')[0]['class']
            name_string = ' '.join(name)
            name_list.append(name_string)
        authors_names_string = ', '.join(name_list)
        return authors_names_string
    
    @property
    def abstract_info(self):
        abstract = self.txt.select('.abstract')[0].find('p').text
        return abstract
    
    @property
    def keywords(self):
        url = 'http://ieeexplore.ieee.org' + self.txt.a['href']
        headers = {
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
           }
        res = requests.get(url=url,headers=headers)
        soup = BeautifulSoup(res.text,'lxml')
        keywords_div = soup.select('#abstractKeywords')
        keyword_a_list = keywords_div[0].findAll('a')
        keyword_str = ''
        for keyword_a in keyword_a_list:
            keyword_str += (keyword_a.text+',')
        return keyword_str
