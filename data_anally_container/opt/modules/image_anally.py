import easyocr


def _read_text_from_image(source_path: str) -> list:
    """画像から文字列を読み込む

    Args:
        image (Image.ImageFile): 対象の画像
        lang (str): 読み取り言語

    Returns:
        str: 画像の読み取り結果
    """
    reader = easyocr.Reader(['ja', 'en'])
    return reader.readtext(source_path, detail=0)


def image_anally(source_path: str) -> list:
    """画像解析して解析結果を返す

    Args:
        source_path (str): 解析対象のイメージパス

    Returns:
        list: 解析結果
    """
    return _read_text_from_image(source_path)
