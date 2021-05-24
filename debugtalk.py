import time

from httprunner import __version__

username = 'zhaoxingkuan'
password = '12345678'


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_time():
    print(round(time.time() * 1000))


def get_username(n):
    print(n)
    return 'zhaoxiongkuan'


def get_password():
    return '12345678'


if __name__ == '__main__':
    print(get_httprunner_version())
    print(get_time())
    print(get_username())
    print(get_password())
