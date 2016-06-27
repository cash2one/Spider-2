#coding:utf-8
__author__ = 'Administrator'

from WeiboSpider import SeleniumWeiboCatch
import time
import random

if __name__=='__main__':
    spider = SeleniumWeiboCatch()
    file = open('record.txt','a')
    spider.login('luyangaini@vip.qq.com','kidlin')
    user_foo = [
        {'id':'277772655','buffer':None},
        {'id':'5360104594','buffer':None},
        {'id':'5842071290','buffer':None},
    ]

    def init_success(user_foo):
        for user in user_foo:
            if not user['buffer']:
                return False
        print('init_success')
        return True

    while(1):
        if init_success(user_foo):
            break
        for user in user_foo:
            if not user['buffer']:
                user['buffer'] = spider.catch_info(user['id'])[1]


    while(1):
        user = random.choice(user_foo)
        info = spider.catch_info(user['id'])
        latest_weibo = info[1]
        print 'the latest weibo:',latest_weibo
        if latest_weibo!=user['buffer']:
            print('DIFF\N:')
            print 'BACK:',user['buffer']
            print 'NEW:',latest_weibo
            user['buffer'] = latest_weibo
            spider2 = SeleniumWeiboCatch()
            spider2.get_png(user['id'])
            spider2.tearDown()
            subject = 'New Weibo!'
            content = info[0] + info[1]
            content += '\nplease check in http://weibo.com/u/'+ user['id'] + '?is_all=1'
            spider.send_mail(subject,content,file)
        time.sleep(random.randint(5,10))
        print('search_again')
    spider.tearDown()


