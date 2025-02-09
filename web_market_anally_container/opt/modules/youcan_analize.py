import re
from modules.web_anally_mng import analizeUrlBase
from common.log_decorator import logger
from common import const


ROOT_URL = r'https://www.u-can.co.jp'
TOP_MENU_URL = r'https://www.u-can.co.jp/course/?il=[course]top_leftmenu'
COURSE_SECTION_BLOCK_CLASS = r'course section-block'
COURSE_INNER_CLASS = r'course__inner'
COURSE_LIST_CLASS = r'course-list'
COURSE_LIST_LINK = r'course-list__link'

class youcanAnalize(analizeUrlBase):
    def __init__(self):
        super().__init__(TOP_MENU_URL)
        self.course_defail_list = []
        self.analize()

    def analize(self):
        """ユーキャンの商品ページ解析
        """
        # カテゴリごとにリスト化
        self.course_category_list = self.body.find('section', class_=COURSE_SECTION_BLOCK_CLASS) \
            .find_all('div', class_=COURSE_INNER_CLASS)
        for course_category in self.course_category_list:
            # カテゴリ内の商品リストを取得
            course_list = course_category.find('ul', class_=COURSE_LIST_CLASS).find_all('li', class_='course-list__item')
            for course in course_list:
                ret = self.analize_course(course)
                logger.debug(const.COURSE_INFO_MSG.format(
                    course_name=ret['course_name'],
                    course_ammount=ret['course_ammount'],
                    course_link=ret['course_link']
                ))
                self.course_defail_list.append(ret)

    
    def analize_course(self, course):
        """ユーキャンの講座の詳細ページの解析
        """
        # 商品情報のURLリンクを取得
        a = course.find('a', class_=COURSE_LIST_LINK)
        course_name = a.find('span', 'course-list__text').text
        course_detail_link = ROOT_URL + a.attrs['href']
        # リンク先のページ情報を取得
        title, body = self.get_html_from_url(course_detail_link)
        # 商品価格を取得
        cost = body.find('span', class_='cost-text')
        ammount = '0'
        if cost:
            total_ammount = cost.find('span', class_='cost-text__ammount').text
            ammount = re.search(r'総計:(?P<ammount>\d+,\d+)円', total_ammount).group('ammount') \
                .replace(',', '')

        return {
            'course_name': course_name,
            'course_ammount': ammount,
            'course_link': course_detail_link
        }
