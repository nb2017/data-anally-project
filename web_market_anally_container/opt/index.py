from common.log_decorator import log_execution, logger
from modules.youcan_analize import youcanAnalize, analizeUrlBase


@log_execution
def main():
    youcanAnalize()


if __name__ == "__main__":
    main()
