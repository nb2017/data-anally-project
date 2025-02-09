from common import const
import logging
import os
import json
from functools import wraps


# ログディレクトリが存在しない場合は作成
if not os.path.exists(const.LOG_DIR):
    os.makedirs(const.LOG_DIR)

format = "%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s"

with open(const.LOG_CONFIG_JSON_PATH, 'r') as f:
    log_conf = json.load(f)
    logger = logging.getLogger(__name__)
    logger.setLevel(const.LOG_LEVEL[log_conf['level']])
    st_handler = logging.StreamHandler()
    st_handler.setFormatter(logging.Formatter(log_conf['formatters']['format']))
    st_handler.setLevel(const.LOG_LEVEL[log_conf['level']])
    fl_handler = logging.FileHandler(filename=const.LOG_PATH, mode=log_conf['filemode'], encoding="utf-8")
    fl_handler.setLevel(const.LOG_LEVEL[log_conf['level']])
    fl_handler.setFormatter(logging.Formatter(log_conf['formatters']['format']))
    logger.addHandler(st_handler)
    logger.addHandler(fl_handler)


# デコレータの定義
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'開始: {func.__name__} の処理を開始しました。')
        result = func(*args, **kwargs)
        logger.info(f'終了: {func.__name__} の処理が完了しました。')
        return result
    return wrapper
