#coding:utf-8
import requests
from bs4 import BeautifulSoup

class ArticleModel_IEEE(object):
    def __init__(self, article_area):
        self.article_area = article_area
        self.txt = self.article_area.select('.txt')[0]
        self.pdf_url = None
        self.html_url = None
    
    def pdf_html_url_dectector(self):
        div_control = self.article_area.select('.controls')[0]
        href_list = div_control.select('a[href]')
        for i in href_list:
            
            href = i['href']
            if href != '#':
                href = str(href)
                if href.startswith('/stamp'):
                    self.pdf_url = href
                elif href.startswith('/xpls'):
                    self.html_url = href
                else:
                    pass
    
    def show_in_cmd(self):
        self.pdf_html_url_dectector()
        print('Title:',self.title)
        print('Author:',self.author)
        print('Pdf_Url:',self.pdf_url)
        print('Html_Url:',self.html_url)
        print('Abstract_Info:',self.abstract_info)
        print('----------------')

    @property
    def title(self):
        span = self.txt.find('span')
        try:
            title_string = span.text
            title_string = str(title_string)
        except:
            title_string = None
        return title_string
    
    @property
    def author(self):
        authors = self.txt.select('.authors')[0]
        name_area = authors.select('.authorPreferredName')
        author_group_string = ''
        for name in name_area:
            name =  name.select('#preferredName')[0]['class']
            author_group_string += str(name)
        if author_group_string:
            pass
        else:
            author_group_string = None
        return author_group_string
    
    @property
    def abstract_info(self):
        try:
            abstract = self.txt.select('.abstract')[0].find('p').text
            abstract = str(abstract)
        except:
            abstract = None
        return abstract

        

def Analize_per_page(http_address):
    response = requests.get(http_address)
    soup = BeautifulSoup(response.text)
    mainarea = soup.select('.results')
    try:
        for article_area in mainarea[0]. select('li'):
            ArticleObj = ArticleModel_IEEE(article_area)
            ArticleObj.show_in_cmd()
    except:
        pass
       
    
if __name__ == '__main__':
    links_list = []
    for line in open("links.txt"):
        links_list.append(line)
    for page_link in links_list:
        print(page_link)
        Analize_per_page(page_link)
        print ('========================================')
    print("over!")    
    
