import logging

LOG_CONFIG_JSON_PATH = r'./log_config.json'
LOG_DIR = 'logs'
LOG_FILE = 'youtube_anally.log'
LOG_PATH = f'{LOG_DIR}/{LOG_FILE}'
LOG_LEVEL = {
    'DEBUG': logging.DEBUG,
    'WARN': logging.WARN,
    'ERROR': logging.ERROR,
    'INFO': logging.INFO
}

MAX_RESULT = 1000

CONFIG_INI_PATH = r'./config.ini'

SNAP_INFO_MSG = '動画タイトル: {title}, チャンネル名: {channel}, リンク: {link}, サムネイル: {thumbnail}'

