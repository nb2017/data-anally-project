import json


def _read_json_file(json_path: str) -> str:
    """JSONファイル読み込み

    Args:
        json_path (str): JSNOファイルパス

    Returns:
        str: ファイル読み込み結果
    """
    ret = ''
    with open(json_path, encoding='utf-8') as f:
        ret = f.read()
    return ret

def get_json_dict(json_path: str) -> dict:
    return json.load(_read_json_file(json_path))
