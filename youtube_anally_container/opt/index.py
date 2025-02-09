from googleapiclient.discovery import build
from common import const
from common.log_decorator import log_execution, logger
import configparser

#ConfigParserオブジェクトを生成
config = configparser.ConfigParser()
#設定ファイル読み込み
config.read(const.CONFIG_INI_PATH)


def _youtube_anally(key_word: str):
    api_key = config['YouTube']['API_KEY']
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_responses = youtube.search().list(
        q=key_word,
        part='snippet',
        type='video',
        regionCode="jp",
        maxResults=const.MAX_RESULT,
    ).execute()
    for search_response in search_responses['items']:
        # snippet
        snippetInfo = search_response['snippet']
        # 動画タイトル
        title = snippetInfo['title']
        # チャンネル名
        channeltitle = snippetInfo['channelTitle']
        # リンク
        link = f"https://www.youtube.com/watch?v={search_response['id']}"
        # サムネイル
        thumbnail = search_response['snippet']['thumbnails']['high']['url']
        logger.debug(const.SNAP_INFO_MSG.format(title=title, channel=channeltitle, link=link, thumbnail=thumbnail))


@log_execution
def main():
    _youtube_anally('エンジニア')


if __name__ == "__main__":
    main()
