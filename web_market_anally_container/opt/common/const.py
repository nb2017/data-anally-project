import logging

LOG_CONFIG_JSON_PATH = r'./log_config.json'
LOG_DIR = 'logs'
LOG_FILE = 'web_market_anally.log'
LOG_PATH = f'{LOG_DIR}/{LOG_FILE}'
LOG_LEVEL = {
    'DEBUG': logging.DEBUG,
    'WARN': logging.WARN,
    'ERROR': logging.ERROR,
    'INFO': logging.INFO
}

