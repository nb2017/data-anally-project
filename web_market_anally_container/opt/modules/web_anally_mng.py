import requests
from bs4 import BeautifulSoup as bs
from bs4.element import Tag

class analizeUrlBase():
    def __init__(self, url):
        self.course_defail_list = []
        self.service = ''
        title, body = self.get_html_from_url(url)
        if title and body:
            self.title = title
            self.body = body

    def get_html_from_url(self, url: str) -> tuple[Tag, Tag]:
        """対象のURLの解析したHTMLを取得

        Args:
            url (str): 対象のURLの

        Returns:
            tuple: 解析したHTMLのtitleとbody
        """
        r = requests.get(url)
        r.encoding = 'utf-8'
        html = r.text
        # HTMLを解析
        soup = bs(html, 'html.parser')

        # 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
        title = soup.find("title")
        body = soup.find("body")
        return title, body
    
    def get_anallized_data(self) -> list:
        return self.course_defail_list
