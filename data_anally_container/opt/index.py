
import sys
import json
import os
from modules import image_anally as ia
from modules.log_decorator import log_execution
from common import const, util
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
def main(args: list[str]) -> int:
    """画像解析検証用のコンテナメイン処理

    Args:
        args (list[str]): 引数

    Returns:
        int: 正常 0、異常 -1
    """

    try:
        ret = ia.image_anally(args[1])
        logger.info(f'読み取り結果 = {ret}')

    except Exception as e:
        logger.error(e)
        return -1
    finally:
        pass
    return 0

if __name__ == '__main__':
    main(sys.argv)