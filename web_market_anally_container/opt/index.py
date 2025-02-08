import json
import os

from common import const
from modules.log_decorator import log_execution
from modules.youcan_analize import youcanAnalize
from logging import getLogger, config


# ログディレクトリが存在しない場合は作成
if not os.path.exists(const.LOG_DIR):
    os.makedirs(const.LOG_DIR)


with open(const.LOG_CONFIG_JSON_PATH, 'r') as f:
    log_conf = json.load(f)
    log_conf['handlers']['fileHandler']['filename'] = const.LOG_PATH

config.dictConfig(log_conf)
logger = getLogger(__name__)


@log_execution
def main():
    youcan = youcanAnalize()


if __name__ == "__main__":
    main()
