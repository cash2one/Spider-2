from stringHandleByMyself import stripWithParamString

class DoubanMovie250(object):
    def __init__(self,movie_li_html):
        self.movie_item = movie_li_html.select('.item')[0]
        self.main_role = ''
        self.birth = ''
        self.area_list = []
        self.director = ''
        self.tag_list = []
        #开局直接运行解析内核
        self.detailParseCoreRun()
          
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
    
    def detailParseCoreRun(self):
        detail_string = self.movie_item.select('.bd')[0].find('p').text
        detail_list = detail_string.split('\xa0')
        info_list = []
        for item in detail_list:
            if item != '/' and item != '':
                info_list.append(item)
        director_string = info_list[0]
        director_string = stripWithParamString(director_string, '\n 导演：,,: ')
        self.director = director_string
        #处理主角以及年代
        t = info_list[1].split('\n')
        main_role_string = t[0]
        self.main_role = stripWithParamString(main_role_string,'主演: ')
        self.birth = t[1].strip(' ')
        #地区列表生成，首先去换行符
        area_list = info_list[2].split(' ')
        for area in area_list:
            if area:
                area = area.strip('\n')
                self.area_list.append(area)
            else:
                break
        #标签列表生成，首先去换行符
        tag_list = info_list[3].split(' ')
        for tag in tag_list:
            if tag:
                tag = tag.strip('\n')
                self.tag_list.append(tag)
            else:
                break

    def show_info(self):
        #信息输出
        print('PicSrc:\t',self.pic_src)
        print('Title:\t',self.title)
        print('Introd_url:\t',self.introduction_url)
        print('Score:\t',self.score)
        print('Comment:\t',self.comment)
        print('Director:\t',self.director)
        print('MainRole:\t',self.main_role)
        print('Area_list:\t',self.area_list)
        print('Tag_list:\t',self.tag_list)
        print('Birth:\t',self.birth)
    
    def save_to_database(self):
        pass
    
    
