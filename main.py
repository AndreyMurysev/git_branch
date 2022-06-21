from loguru import logger


def hello_world():
    print('Hello World')
    logger.debug("code200")


if __name__ == '__main__':
    hello_world()
