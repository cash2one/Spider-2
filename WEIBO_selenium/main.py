#coding:utf-8
__author__ = 'Administrator'

from WeiboSpider import SeleniumWeiboCatch
import time
import random

if __name__=='__main__':
    user_foo = [
        {'id':'277772655','buffer':2},
        {'id':'5360104594','buffer':1},
        {'id':'5842071290','buffer':3},
    ]

    spider = SeleniumWeiboCatch()
    file = open('record.txt')
    spider.login('luyangaini@vip.qq.com','kidlin')
    time.sleep(3)
    spider.get_png()


    '''
    def init_success(user_foo):
        for user in user_foo:
            if not user['buffer']:
                return False
        return True

    while(1):
        if init_success(user_foo):
            break
        for user in user_foo:
            if not user['buffer']:
                try:
                    info = spider.catch_info(user['id'])
                    if info[0][:2]=='置顶':
                        user['buffer'] = info[1]
                    else:
                        user['buffer'] = info[0]
                except:
                    pass

    while(1):
        for user in user_foo:
            print(user['id'])
            while(1):
                info = spider.catch_info(user['id'])
                if info:
                   break
            latest_tweet = ''
            if info[0][:2]=='置顶':
                latest_tweet = info[1]
            else:
                latest_tweet = info[0]
            if latest_tweet!=user['buffer']:
                print('DIFF!!!!!')
                print ('BACK:',user['buffer'])
                print ('NEW:',latest_tweet)
                user['buffer'] = latest_tweet
                spider.get_png()
                subject = 'New Weibo!'
                content = latest_tweet
                content += '\nplease check in http://weibo.com/u/'+ user['id'] + '?is_all=1'
                spider.send_mail(subject,content,file)
            else:
                print('Same!')
                print ('BACK and NEW both is:',latest_tweet)
            time.sleep(random.randint(2,5))
        print('All users checked.  Search again...\n')

    spider.tearDown()
    '''
