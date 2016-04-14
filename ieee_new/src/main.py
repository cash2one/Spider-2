from bs4 import BeautifulSoup
import requests

url = 'http://ieeexplore.ieee.org/xpl/abstractAuthors.jsp?arnumber=766880&filter%3DAND%28p_IS_Number%3A16611%29%26pageNumber%3D2'
headers = {
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
           }

res = requests.get(url=url,headers=headers)

soup = BeautifulSoup(res.text,'lxml')

author_div = soup.select('#abstractAuthors')

keywords_div = soup.select('#abstractKeywords')

print(author_div)

print(keywords_div)

keyword_a_list = keywords_div[0].findAll('a')

keyword_str = ''

for keyword_a in keyword_a_list:
    keyword_str += (keyword_a.text+',')
    
print(keyword_str)
