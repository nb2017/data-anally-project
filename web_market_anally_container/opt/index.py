from common import const
from common.log_decorator import log_execution, logger
from modules.youcan_analize import youcanAnalize, analizeUrlBase
import requests
import configparser

#ConfigParserオブジェクトを生成
config = configparser.ConfigParser()
#設定ファイル読み込み
config.read(const.CONFIG_INI_PATH)


def _post_anally_data(anally_service_list: list[analizeUrlBase]):
    for service in anally_service_list:
        # GASのウェブアプリURL
        GAS_URL = config['Google']['GAS_URL']
        # 送信するデータ
        payload = {
            "spreadsheetId": config['Google']['SPREAD_SHEET_ID'],
            "service": service.service,
            "data": service.get_anallized_data()
        }
            # POSTリクエストを送信
        response = requests.post(GAS_URL, json=payload)
        # レスポンスの表示
        logger.info(f"Response from GAS: {response.text}")


@log_execution
def main():
    anally_service_list :list[analizeUrlBase]= [] 
    anally_service_list.append(youcanAnalize())
    _post_anally_data(anally_service_list)


if __name__ == "__main__":
    main()
