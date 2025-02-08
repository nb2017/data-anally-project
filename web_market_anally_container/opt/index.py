from common.log_decorator import log_execution
from modules.youcan_analize import youcanAnalize


@log_execution
def main():
    youcan = youcanAnalize()


if __name__ == "__main__":
    main()
