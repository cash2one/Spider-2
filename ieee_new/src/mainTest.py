"""
    author: Lu Yang
"""
# coding:utf-8

import requests
from bs4 import BeautifulSoup
from IEEEArticleClass import *
'''
import os
import socket
import socks
from multiprocessing.dummy import Pool as ThreadPool
from random import randint
import time
'''
def parse_page(http_address):
    '''
    random_port = lambda l, r: randint(l, r)
    port = random_port(9053, 9073)
    print(time.ctime())
    time.sleep(2)
    '''
    mainarea = None
    '''
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", port)
    socket.socket = socks.socksocket
    '''
    response = requests.get(http_address, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'})
    soup = BeautifulSoup(response.text, "lxml")
    mainarea = soup.select('.results')
    if mainarea:
        article_list = mainarea[0].select('li')
        for article in article_list:
            try:
                articleObj = IEEE_Artile(article)
                articleObj.show_in_cmd()
                #articleObj.save_to_database()
            except Exception as err:
                print(err)
            
            print('---------')
            
         
if __name__ == '__main__':
    url = 'http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=6776147&filter=AND(p_IS_Number:6776147)&pageNumber=1'
    parse_page(url)
    '''
    links_list = []
    for line in open("links.txt.2"):
        links_list.append(line)
    #pool = ThreadPool(8)
    results = pool.map(parse, links_list)
    #pool.close()
    #pool.join()
    '''