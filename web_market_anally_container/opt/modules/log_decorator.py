from common import const
import logging
import os
import json
from functools import wraps
from logging import getLogger, config


# ログディレクトリが存在しない場合は作成
if not os.path.exists(const.LOG_DIR):
    os.makedirs(const.LOG_DIR)


with open(const.LOG_CONFIG_JSON_PATH, 'r') as f:
    log_conf = json.load(f)
    log_conf['handlers']['fileHandler']['filename'] = const.LOG_PATH

config.dictConfig(log_conf)
logger = getLogger(__name__)



# ログディレクトリが存在しない場合は作成
if not os.path.exists(const.LOG_DIR):
    os.makedirs(const.LOG_DIR)


# ログ設定
logging.basicConfig(
    filename=const.LOG_PATH,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)


# デコレータの定義
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'開始: {func.__name__} の処理を開始しました。')
        result = func(*args, **kwargs)
        logging.info(f'終了: {func.__name__} の処理が完了しました。')
        return result
    return wrapper
