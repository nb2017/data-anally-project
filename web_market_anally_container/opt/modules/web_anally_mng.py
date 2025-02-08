import requests
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from modules.log_decorator import logger

class analizeUrlBase():
    def __init__(self, url):
        title, body = self.get_html_from_url(url)
        if title is None or body is None:
            pass
        else:
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
        logger.debug(f'requests response = {r}')
        # HTMLを解析
        soup = bs(r.text, 'html.parser')

        # 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
        title = soup.find("title")
        body = soup.find("body")
        return title, body
