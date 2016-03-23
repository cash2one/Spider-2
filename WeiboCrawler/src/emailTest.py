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
            'cookie':'SUHB=0pHhOPHjFBWmE9; _T_WM=bef2c515f1bcb67425331213a5262a1b; gsid_CTandWM=4udVa35c1dW73448sBMwdbi7q6b; SUB=_2A2579h9tDeRxGeRI4lMT9i7Pwz-IHXVZGKElrDV6PUJbrdANLUv2kW1LHetUTXME6KB2kvAjU18PpbyLbiGYBA..',
            'cookie_user_id':'2691260383',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'           
       }
headers_kidlin = {
            'cookie':'_T_WM=9c937db8943c8dc9bd404af31c6a9034; gsid_CTandWM=4u2lb1311aM2iATFPEn7coH4V9v; SUB=_2A2579h_XDeTxGeNG41cV9ifJwzWIHXVZGKGfrDV6PUJbrdANLVrBkW1LHetI9q14HWFoRAqzd80tByOK6IR9LQ..',
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


# content = '<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="Cache-Control" content="no-cache"><meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0"><link rel="icon" sizes="any" mask="" href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" color="black"><meta name="MobileOptimized" content="240"><title>科普君XueShu的微博</title><style type="text/css" id="internalStyle">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></head><body><div class="n" style="padding: 6px 4px;"><a href="http://weibo.cn/?tf=5_009" class="nl">首页</a>|<a href="http://weibo.cn/msg/?tf=5_010" class="nl">消息</a>|<a href="http://huati.weibo.cn" class="nl">话题</a>|<a href="http://weibo.cn/search/?tf=5_012" class="nl">搜索</a>|<a href="/xuebaxueshu?rand=1201&amp;p=r" class="nl">刷新</a></div><div class="u"><table><tbody><tr><td valign="top"><a href="/5097174964/avatar?rl=0"><img src="http://tp1.sinaimg.cn/5097174964/50/5747416205/1" alt="头像" class="por"></a></td><td valign="top"><div class="ut"><span class="ctt">科普君XueShu<img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><a href="http://vip.weibo.cn/?F=W_tq_zsbs_01"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M"></a>&nbsp;男/其他    &nbsp;    <span class="cmt">已关注</span></span><br><span class="ctt">认证：微博知名科普视频博主 微博签约自媒体</span><br><span class="ctt" style="word-break:break-all; width:50px;">让科学酷炫起来！</span><br><a href="/im/chat?uid=5097174964&amp;rl=0">私信</a>&nbsp;<a href="/5097174964/info">资料</a>&nbsp;<a href="/5097174964/operation?rl=0">操作</a>&nbsp;<a href="/attgroup/special?fuid=5097174964&amp;st=f2dff9">特别关注</a>&nbsp;<a href="http://new.vip.weibo.cn/vippay/payother?present=1&amp;action=comfirmTime&amp;uid=5097174964">送Ta会员</a></div></td></tr></tbody></table><div class="tip2"><span class="tc">微博[1181]</span>&nbsp;<a href="/5097174964/follow">关注[946]</a>&nbsp;<a href="/5097174964/fans">粉丝[745710]</a>&nbsp;<a href="/attgroup/opening?uid=5097174964">分组[2]</a>&nbsp;<a href="/at/weibo?uid=5097174964">@他的</a></div></div><div class="u"><div class="tc tip2">他的粉丝还关注:<a href="/u/1342704701">噗尺</a>&nbsp;<a href="/u/1672335485">柳三便</a>&nbsp;<a href="/u/2984695154">中二化学于老师</a>&nbsp;<a href="/5097174964/fans?f=suggest">更多&gt;&gt;</a></div></div><div class="pmst"><span class="pms">&nbsp;微博&nbsp;</span><span class="pmsl">&nbsp;<a href="/5097174964/photo?tf=6_008">相册</a>&nbsp;</span></div><div class="pms">全部-<a href="/xuebaxueshu?filter=1">原创</a>-<a href="/xuebaxueshu?filter=2">图片</a>-<a href="/attgroup/opening?uid=5097174964">分组</a>-<a href="/5097174964/search?f=u&amp;rl=0">筛选</a></div><div class="c" id="M_D4Ml23exA"><div>[<span class="kt">置顶</span>]<span class="ctt">你一定好奇过，进入黑洞的过程到底是怎样的。一起来感受一下我听译的《进入黑洞之旅》吧。短短几分钟领略种种精彩与魔幻。 <a href="http://weibo.cn/pages/100808topic?extparam=%E9%85%B7%E7%82%AB%E7%A7%91%E6%99%AE%E5%B0%8F%E7%9F%AD%E7%89%87&amp;from=feed">#酷炫科普小短片#</a>【第31期】<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRUuwOF9&amp;ep=D4Ml23exA%2C5097174964%2CD4Ml23exA%2C5097174964">http://t.cn/RUuwOF9</a></span>&nbsp;<a href="http://weibo.cn/attitude/D4Ml23exA/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[6600]</a>&nbsp;<a href="http://weibo.cn/repost/D4Ml23exA?uid=5097174964&amp;rl=0">转发[13494]</a>&nbsp;<a href="http://weibo.cn/comment/D4Ml23exA?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[1803]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/D4Ml23exA?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">2015-11-20 23:03:34&nbsp;来自微博 weibo.com</span></div></div><div class="s"></div><div class="c" id="M_DntNikrQp"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/lovecomics2013">爆漫画</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">【分手后，男生还会想起女生吗？】如果舍不得，那请别轻易放开她的手。珍惜眼前人[心]<a href="http://weibo.cn/pages/100808topic?extparam=%E6%9C%A8%E6%9C%A8%E7%88%B1%E6%83%85%E6%BC%AB%E7%94%BB&amp;from=feed">#木木爱情漫画#</a></span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/DntukvKo4?rl=1">组图共9张</a>]</div><div><a href="http://weibo.cn/mblog/pic/DntukvKo4?rl=0"><img src="http://ww4.sinaimg.cn/wap180/cd38d15cgw1f25sf80uo4j20hs11b771.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=DntukvKo4&amp;u=cd38d15cgw1f25sf80uo4j20hs11b771">原图</a>&nbsp;<span class="cmt">赞[129]</span>&nbsp;<span class="cmt">原文转发[281]</span>&nbsp;<a href="http://weibo.cn/comment/DntukvKo4?rl=0#cmtfrm" class="cc">原文评论[79]</a><!----></div><div><span class="cmt">转发理由:</span>你怎么看[思考]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DntNikrQp/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DntNikrQp?uid=5097174964&amp;rl=0">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DntNikrQp?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DntNikrQp?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">1分钟前</span></div></div><div class="s"></div><div class="c" id="M_DntMHEJQW"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/575223374">壮士来一发嘛</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">【听到隔壁OOXX是一种什么样的体验】在家、租房、出门住酒店，有时候总会听到一些听不懂的声音（因为我还是个9岁的孩子啊[doge]）...在这个时候....<a href="http://weibo.cn/pages/100808topic?extparam=%E6%B7%B1%E5%A4%9C%E7%97%B4%E5%97%94&amp;from=feed">#深夜痴嗔#</a></span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/DntxzvgE7?rl=1">组图共9张</a>]</div><div><a href="http://weibo.cn/mblog/pic/DntxzvgE7?rl=0"><img src="http://ww4.sinaimg.cn/wap180/67e8c7fdjw1f25ygafvryj20ku33wgz9.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=DntxzvgE7&amp;u=67e8c7fdjw1f25ygafvryj20ku33wgz9">原图</a>&nbsp;<span class="cmt">赞[486]</span>&nbsp;<span class="cmt">原文转发[551]</span>&nbsp;<a href="http://weibo.cn/comment/DntxzvgE7?rl=0#cmtfrm" class="cc">原文评论[656]</a><!----></div><div><span class="cmt">转发理由:</span>感觉是奇妙的体验[doge]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DntMHEJQW/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[2]</a>&nbsp;<a href="http://weibo.cn/repost/DntMHEJQW?uid=5097174964&amp;rl=0">转发[3]</a>&nbsp;<a href="http://weibo.cn/comment/DntMHEJQW?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[1]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DntMHEJQW?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">2分钟前</span></div></div><div class="s"></div><div class="c" id="M_DntG5wfbC"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/u/2726601057">进击的阿木君</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">《红辣椒》可以说是动画版的《盗梦空间》，却又早了四年。“相对于深远的梦境来说，科学可能不过是一堆垃圾而已。”今敏这种天才连上帝都会嫉妒。<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRybrK6e&amp;ep=DntG5wfbC%2C5097174964%2CDntuJ3e5Z%2C2726601057">http://t.cn/RybrK6e</a></span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/DntuJ3e5Z?rl=1">组图共9张</a>]</div><div><a href="http://weibo.cn/mblog/pic/DntuJ3e5Z?rl=0"><img src="http://ww2.sinaimg.cn/wap180/a284a161gw1f25u34ho0zg20a004tnmn.gif" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=DntuJ3e5Z&amp;u=a284a161gw1f25u34ho0zg20a004tnmn">原图</a>&nbsp;<span class="cmt">赞[323]</span>&nbsp;<span class="cmt">原文转发[1064]</span>&nbsp;<a href="http://weibo.cn/comment/DntuJ3e5Z?rl=0#cmtfrm" class="cc">原文评论[82]</a><!----></div><div><span class="cmt">转发理由:</span>马住 //<a href="/n/%E7%94%B5%E5%BD%B1%E6%80%AA%E5%AE%A2">@电影怪客</a>:非常好的动画电影&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DntG5wfbC/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[166]</a>&nbsp;<a href="http://weibo.cn/repost/DntG5wfbC?uid=5097174964&amp;rl=0">转发[170]</a>&nbsp;<a href="http://weibo.cn/comment/DntG5wfbC?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[19]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DntG5wfbC?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">19分钟前</span></div></div><div class="s"></div><div class="c" id="M_Dntv4BNjx"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/xuebaxueshu">科普君XueShu</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">人体的血管</span></div><div><a href="http://weibo.cn/mblog/pic/DnsMbo5cf?rl=0"><img src="http://ww2.sinaimg.cn/wap180/005yXe3qgw1f25wfmqjh3j30go0p0tbo.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=DnsMbo5cf&amp;u=005yXe3qgw1f25wfmqjh3j30go0p0tbo">原图</a>&nbsp;<span class="cmt">赞[2200]</span>&nbsp;<span class="cmt">原文转发[5246]</span>&nbsp;<a href="http://weibo.cn/comment/DnsMbo5cf?rl=0#cmtfrm" class="cc">原文评论[1150]</a><!----></div><div><span class="cmt">转发理由:</span>[笑cry]//<a href="/n/Little__HAN">@Little__HAN</a>：伍迪·艾伦说过，人的血液有限，不能同时用来运行下体和大脑。原来大脑的血管如此密集，难怪人们都喜欢fuck不喜欢think,思考是比较累的!&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dntv4BNjx/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[312]</a>&nbsp;<a href="http://weibo.cn/repost/Dntv4BNjx?uid=5097174964&amp;rl=0">转发[250]</a>&nbsp;<a href="http://weibo.cn/comment/Dntv4BNjx?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[63]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dntv4BNjx?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">46分钟前</span></div></div><div class="s"></div><div class="c" id="M_DnttVr1fs"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/520525025">啪几下</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">小啪餐大食谱，你最爱哪一道前戏菜？[羞嗒嗒]<a href="http://weibo.cn/pages/100808topic?extparam=%E5%95%AA%E5%95%AA%E5%A4%9C%E8%AF%9D&amp;from=feed">#啪啪夜话#</a></span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/Dnt5YiLwR?rl=1">组图共9张</a>]</div><div><a href="http://weibo.cn/mblog/pic/Dnt5YiLwR?rl=0"><img src="http://ww4.sinaimg.cn/wap180/672c0d86jw1f25ujvmpysj20m81ccn2c.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=Dnt5YiLwR&amp;u=672c0d86jw1f25ujvmpysj20m81ccn2c">原图</a>&nbsp;<span class="cmt">赞[415]</span>&nbsp;<span class="cmt">原文转发[1311]</span>&nbsp;<a href="http://weibo.cn/comment/Dnt5YiLwR?rl=0#cmtfrm" class="cc">原文评论[494]</a><!----></div><div><span class="cmt">转发理由:</span>【两性科普】食色性也（The desire for food and sex is part of human nature）——Einstein[doge]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DnttVr1fs/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[44]</a>&nbsp;<a href="http://weibo.cn/repost/DnttVr1fs?uid=5097174964&amp;rl=0">转发[30]</a>&nbsp;<a href="http://weibo.cn/comment/DnttVr1fs?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[72]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DnttVr1fs?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">49分钟前&nbsp;来自微博 weibo.com</span></div></div><div class="s"></div><div class="c" id="M_DntpBrlWl"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/torinouta">夏影</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">这谁设计的蛋黄分离器啊，出来绝对不打你！[拜拜]</span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/Dnt6DouJh?rl=1">组图共2张</a>]</div><div><a href="http://weibo.cn/mblog/pic/Dnt6DouJh?rl=0"><img src="http://ww3.sinaimg.cn/wap180/4b807446gw1f25xw2gnefj20go0gomxt.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=Dnt6DouJh&amp;u=4b807446gw1f25xw2gnefj20go0gomxt">原图</a>&nbsp;<span class="cmt">赞[519]</span>&nbsp;<span class="cmt">原文转发[3878]</span>&nbsp;<a href="http://weibo.cn/comment/Dnt6DouJh?rl=0#cmtfrm" class="cc">原文评论[1069]</a><!----></div><div><span class="cmt">转发理由:</span>[哈哈]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DntpBrlWl/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[264]</a>&nbsp;<a href="http://weibo.cn/repost/DntpBrlWl?uid=5097174964&amp;rl=0">转发[143]</a>&nbsp;<a href="http://weibo.cn/comment/DntpBrlWl?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[57]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DntpBrlWl?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">今天 21:48&nbsp;来自微博 weibo.com</span></div></div><div class="s"></div><div class="c" id="M_DntkXhXMq"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/u/2793823365">表情社</a><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">【英语听力。。】....................................[哆啦A梦微笑]</span>&nbsp;[<a href="http://weibo.cn/mblog/picAll/Dntcy6wAK?rl=1">组图共9张</a>]</div><div><a href="http://weibo.cn/mblog/pic/Dntcy6wAK?rl=0"><img src="http://ww1.sinaimg.cn/wap180/a6865c85jw1f25yapfyw5j207v08jq37.jpg" alt="图片" class="ib"></a>&nbsp;<a href="http://weibo.cn/mblog/oripic?id=Dntcy6wAK&amp;u=a6865c85jw1f25yapfyw5j207v08jq37">原图</a>&nbsp;<span class="cmt">赞[419]</span>&nbsp;<span class="cmt">原文转发[2313]</span>&nbsp;<a href="http://weibo.cn/comment/Dntcy6wAK?rl=0#cmtfrm" class="cc">原文评论[285]</a><!----></div><div><span class="cmt">转发理由:</span>Piece of cake[doge]//<a href="/n/%E6%88%91%E7%9A%84%E5%89%8D%E4%BB%BB%E6%98%AF%E6%9E%81%E5%93%81">@我的前任是极品</a>: 每次听都好慌好慌 //<a href="/n/%E6%97%A0%E6%89%80%E9%A1%BE%E5%BF%8C%E7%9A%84%E5%A4%A7%E5%A6%88">@无所顾忌的大妈</a>:sooooo平时不能记得太多歌[doge][doge][doge]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/DntkXhXMq/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[215]</a>&nbsp;<a href="http://weibo.cn/repost/DntkXhXMq?uid=5097174964&amp;rl=0">转发[169]</a>&nbsp;<a href="http://weibo.cn/comment/DntkXhXMq?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[39]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DntkXhXMq?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">今天 21:36&nbsp;来自微博 weibo.com</span></div></div><div class="s"></div><div class="c" id="M_Dntk96ZOx"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/film35">电影的力量</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">法拉利488 GTB最新短片《JOYRIDE》，巴塞罗那狂飙之夜，超级帅！决定买了！<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRGFP94n&amp;ep=Dntk96ZOx%2C5097174964%2CDnswH4pl9%2C1985375991">http://t.cn/RGFP94n</a></span>&nbsp;<span class="cmt">赞[84]</span>&nbsp;<span class="cmt">原文转发[370]</span>&nbsp;<a href="http://weibo.cn/comment/DnswH4pl9?rl=0#cmtfrm" class="cc">原文评论[51]</a><!----></div><div><span class="cmt">转发理由:</span>假装自己买得起[馋嘴]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dntk96ZOx/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[165]</a>&nbsp;<a href="http://weibo.cn/repost/Dntk96ZOx?uid=5097174964&amp;rl=0">转发[204]</a>&nbsp;<a href="http://weibo.cn/comment/Dntk96ZOx?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[56]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dntk96ZOx?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">今天 21:34</span></div></div><div class="s"></div><div class="c" id="M_Dntc1Ari4"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/ictech">C科技</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">不少果粉自欺欺人，说他喜欢4英寸手机，当初iPhone6是所有iPhone中销量增长最高的，根本原因就是大屏刺激，如果4英寸真的是主流，苹果推出的会是高端4英寸iPhone，售价5288，重新设计外观。给你iPhone6S和iPhoneSE，我就不信你选SE！</span>&nbsp;<span class="cmt">赞[281]</span>&nbsp;<span class="cmt">原文转发[104]</span>&nbsp;<a href="http://weibo.cn/comment/DnqmQtl0t?rl=0#cmtfrm" class="cc">原文评论[345]</a><!----></div><div><span class="cmt">转发理由:</span>你们用的手机4英寸还是4.7英寸[思考]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dntc1Ari4/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[170]</a>&nbsp;<a href="http://weibo.cn/repost/Dntc1Ari4?uid=5097174964&amp;rl=0">转发[41]</a>&nbsp;<a href="http://weibo.cn/comment/Dntc1Ari4?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[173]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dntc1Ari4?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">今天 21:14</span></div></div><div class="s"></div><div class="c" id="M_Dnt82yITy"><div><span class="cmt">转发了&nbsp;<a href="http://weibo.cn/u/3230715380">我的女友嘴很贱</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5338.gif" alt="V"><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">女朋友的语言理解能力我给满分。刘文静，你这是在玩火。<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRGFY7lO&amp;ep=Dnt82yITy%2C5097174964%2CDnt6im1qG%2C3230715380">http://t.cn/RGFY7lO</a>（使用<a href="http://weibo.cn/pages/100808topic?extparam=%E7%A7%92%E6%8B%8D&amp;from=feed">#秒拍#</a>录制）</span>&nbsp;<span class="cmt">赞[1944]</span>&nbsp;<span class="cmt">原文转发[2537]</span>&nbsp;<a href="http://weibo.cn/comment/Dnt6im1qG?rl=0#cmtfrm" class="cc">原文评论[906]</a><!----></div><div><span class="cmt">转发理由:</span>你们想不想我这的科普视频也换成这种中文机器配音[馋嘴]&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dnt82yITy/add?uid=2691260383&amp;rl=0&amp;st=f2dff9">赞[126]</a>&nbsp;<a href="http://weibo.cn/repost/Dnt82yITy?uid=5097174964&amp;rl=0">转发[27]</a>&nbsp;<a href="http://weibo.cn/comment/Dnt82yITy?uid=5097174964&amp;rl=0#cmtfrm" class="cc">评论[68]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dnt82yITy?rl=0&amp;st=f2dff9">收藏</a><!---->&nbsp;<span class="ct">今天 21:05</span></div></div><div class="s"></div><div class="pa" id="pagelist"><form action="/xuebaxueshu" method="post"><div><a href="/xuebaxueshu?page=2">下页</a>&nbsp;<input name="mp" value="115" type="hidden"><input name="page" size="2" style="-wap-input-format: &quot;*N&quot;" type="text"><input value="跳页" type="submit">&nbsp;1/115页</div></form></div><div class="pm"><form action="/search/" method="post"><div><input name="keyword" value="" size="15" type="text"><input name="smblog" value="搜微博" type="submit"><input name="suser" value="找人" type="submit"><br><span class="pmf"><a href="/search/mblog/?keyword=KAT-TUN%E5%8D%81%E5%B9%B4%E7%A5%AD&amp;rl=0" class="k">KAT-TUN十年祭</a>&nbsp;<a href="/search/mblog/?keyword=TFBOYS%E7%8E%8B%E6%BA%90%E6%89%8B%E5%86%99%E5%AD%97%E4%BD%93&amp;rl=0" class="k">TFBOYS王源手写字体</a>&nbsp;<a href="/search/mblog/?keyword=%E8%9D%99%E8%9D%A0%E4%BE%A0%E5%A4%A7%E6%88%98%E8%B6%85%E4%BA%BA&amp;rl=0" class="k">蝙蝠侠大战超人</a>&nbsp;<a href="/search/mblog/?keyword=%E5%90%8C%E9%81%93%E5%A4%A7%E5%8F%94%E4%B8%BA%E5%A4%84%E5%A5%B3%E5%BA%A7%E6%AD%A3%E5%90%8D&amp;rl=0" class="k">同道大叔为处女座正名</a>&nbsp;<a href="/search/mblog/?keyword=%E7%8E%8B%E9%9D%92%E5%B7%A6%E8%80%B3%E8%88%9E%E5%8F%B0%E5%89%A7&amp;rl=0" class="k">王青左耳舞台剧</a></span></div></form></div><div class="cd"><a href="#top"><img src="http://u1.sinaimg.cn/3g/image/upload/0/62/203/18979/5e990ec2.gif" alt="TOP"></a></div><div class="pms"> <a href="http://weibo.cn">首页</a>.<a href="http://weibo.cn/topic/240489">反馈</a>.<a href="http://weibo.cn/page/91">帮助</a>.<a href="http://down.sina.cn/weibo/default/index/soft_id/1/mid/0">客户端</a>.<a href="http://weibo.cn/spam/?rl=0&amp;type=3&amp;fuid=5097174964" class="kt">举报</a>.<a href="http://passport.sina.cn/sso/logout?r=http%3A%2F%2Fweibo.cn%2Fpub%2F%3Fvt%3D&amp;entry=mweibo">退出</a></div><div class="c">设置:<a href="http://weibo.cn/account/customize/skin?tf=7_005&amp;st=f2dff9">皮肤</a>.<a href="http://weibo.cn/account/customize/pic?tf=7_006&amp;st=f2dff9">图片</a>.<a href="http://weibo.cn/account/customize/pagesize?tf=7_007&amp;st=f2dff9">条数</a>.<a href="http://weibo.cn/account/privacy/?tf=7_008&amp;st=f2dff9">隐私</a></div><div class="c">彩版|<a href="http://m.weibo.cn/?tf=7_010">触屏</a>|<a href="http://weibo.cn/page/521?tf=7_011">语音</a></div><div class="b">weibo.cn[03-22 22:47]</div></body></html>'
# send_email('xugelin',content,'html',logObj)

#CrawlSpecificUserFansInfo('1742566624', headers, weiboDB)

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
        elif ret['status'] is 4:
            #invalid cookie
            switch_cookie()
            print('swicth cookie success')
        else:
            pass
    print('\n又要重新爬一遍，好烦\n')