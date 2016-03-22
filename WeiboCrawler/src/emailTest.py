#coding: utf-8  
from mytools.emailClass import Email
import time
from main_func import *
from mytools.MyDatabaseClass import MyDatabase
from mytools.fileClass import File


#'5885469589',
WeiboId_list = ('5885469589','2691260383','5360104594','5842071290')
#WeiboId_list = ('5885469589',)

weiboDB = MyDatabase(host='localhost',user='root',passwd='',db='weibo',port=3306,charset='utf8')

cookie_list = ('SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; gsid_CTandWM=4udVa35c1dW73448sBMwdbi7q6b; SUB=_2A2579JvyDeRxGeRI4lMT9i7Pwz-IHXVZFiW6rDV6PUJbrdANLXDykW1LHesATt0ju3lSVjv4AYl5bImahXQjpw..',

    '_T_WM=9c937db8943c8dc9bd404af31c6a9034; gsid_CTandWM=4u2lb1311aM2iATFPEn7coH4V9v; SUB=_2A2579JxADeTxGeNG41cV9ifJwzWIHXVZFiQIrDV6PUJbrdANLUmmkW1LHeshEnRyH0kdGBqKrCXW8zRtL3wGFQ..')

headers_luyang = {
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; gsid_CTandWM=4udVa35c1dW73448sBMwdbi7q6b; SUB=_2A2579JvyDeRxGeRI4lMT9i7Pwz-IHXVZFiW6rDV6PUJbrdANLXDykW1LHesATt0ju3lSVjv4AYl5bImahXQjpw..',
            'cookie_user_id':'2691260383',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
headers_kidlin = {
            'cookie':'_T_WM=9c937db8943c8dc9bd404af31c6a9034; gsid_CTandWM=4u2lb1311aM2iATFPEn7coH4V9v; SUB=_2A2579JxADeTxGeNG41cV9ifJwzWIHXVZFiQIrDV6PUJbrdANLUmmkW1LHeshEnRyH0kdGBqKrCXW8zRtL3wGFQ..',
            'cookie_user_id':'5885469589',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
                  }

headers_list = (headers_luyang,headers_kidlin)

global headers
headers = headers_list[0]

def switch_cookie():
    global headers
    if headers == headers_list[0]:
        headers = headers_list[1]
    else:
        headers = headers_list[0]
    return

error_cot = 0

logObj = File('log.txt','a')


# content = '<html xmlns="http://www.w3.org/1999/xhtml"><head><meta content="text/html; charset=utf-8" http-equiv="Content-Type"/><meta content="no-cache" http-equiv="Cache-Control"/><meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0" id="viewport" name="viewport"/><link color="black" href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" mask="" rel="icon" sizes="any"><meta content="240" name="MobileOptimized"/><title>微博</title><style id="internalStyle" type="text/css">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></link></head><body><div class="c">登录|<a href="http://weibo.cn/reg/index?backURL=http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1">注册</a><br/></div><div class="c">欢迎访问微博 <a href="http://weibo.cn/reg/faq?c=ttt&amp;backURL=http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1">什么是微博？</a><br/><form action="?rand=432400446&amp;backURL=http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1" method="post"><div>手机号/电子邮箱/会员帐号:<br/><input name="mobile" size="30" type="text" value=""/><br/>密码:(<a href="/login/?backURL=http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1&amp;pt=1">使用明文密码</a>)<br/><input name="password_3014" size="30" type="password"/><br/>请输入图片中的字符:<br/><img alt="请打开图片显示" src="http://weibo.cn/interface/f/ttt/captcha/show.php?cpt=2_719580a7f6fc4bb7"/><br/><input name="code" size="8" type="text" value=""/><br/><input checked="checked" name="remember" type="checkbox"/>记住登录状态，需支持并打开手机的cookie功能。<br/><input name="backURL" type="hidden" value="http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile"/><input name="backTitle" type="hidden" value="微博"/><input name="tryCount" type="hidden" value=""/><input name="vk" type="hidden" value="3014_0ba2_1760035135"/><input name="capId" type="hidden" value="2_719580a7f6fc4bb7"/><input name="submit" type="submit" value="登录"/> <a href="http://weibo.cn/reg/forgetpwd?backURL=http%3A%2F%2Fweibo.cn%2F2691260383%2Fprofile&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1">忘记密码</a><br/><div>使用合作网站帐号登录:<br/><table><tr><td><a href="http://weibo.cn/sinaurl?goto=http%3A%2F%2Fapi.open.uc.cn%2Fauthorize%3Fclient_id%3D20032%26redirect_uri%3Dhttp%253A%252F%252Flogin.weibo.cn%252Flogin%252Fuc_callback%253FbackURL%253Dhttp%25253A%25252F%25252Fweibo.cn%25252F2691260383%25252Fprofile%2526amp%253BbackTitle%253D%2525E5%2525BE%2525AE%2525E5%25258D%25259A%2526amp%253Bvt%253D4%2526amp%253Brevalid%253D2%2526amp%253Bns%253D1%26response_type%3Dcode&amp;signUrl=abff78a7df"><b>UC浏览器</b></a></td></tr></table></div>小提示：<br/>1、登录成功后保存任意页面为书签，下次通过书签访问，也可免去登录过程。<br/><span style="color:red">2、请不要直接通过手机浏览器的发送地址功能将登录后的页面地址发送给朋友，以免泄露个人信息及密码。</span><br/><img alt="" src="http://218.206.86.254/2008/match/c.gif?f=wap_reg" style="display:none"/></div></form></div></body></html>'
# send_email('xugelin',content,'html',logObj)

'''
ret = {'status':-1}
cot = 0
while ret['status']!=3:
    ret = CrawlSpecificUserWeibosInfo('5360104594',headers,weiboDB,cot)
    if ret['status'] == 4:
        switch_cookie()
    else:
        cot += 1
'''
        
while 1: 
    print('error_cot = ',error_cot)
    if error_cot >20:
        switch_cookie()
        error_cot = 0
        print('swicth cookie success')
    for userID in WeiboId_list:
        print(userID)
        ret = CrawlSpecificUserWeibosInfo(userID, headers, weiboDB,page=0)
        if ret['status'] is 1:
            sql = "SELECT username FROM user WHERE account_id=" + userID
            weiboDB.cur.execute(sql)
            author_name_list = weiboDB.cur.fetchall()
            author_name = author_name_list[0][0]
            print(author_name)
            profile_url = 'http://weibo.cn/'+ userID +'/profile'
            content = ret['content']
            send_email(author_name,content,'html',logObj)
        elif ret['status'] is 2:
            error_cot += 1
        elif ret['status'] is 0:
            #invalid cookie
            switch_cookie()
        else:
            pass
    print('\n又要重新爬一遍，好烦\n')
    