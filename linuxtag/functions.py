import requests
import datetime


def add_five(arg: int) -> int:
    return arg + 5


def blubb(arg: bool) -> bool:
    if arg:
        return True
    else:
        return False


# def is_sunday(date: str = ""):
def is_sunday(date: str):
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    # try:
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    return dt.isoweekday() == 7
    # except:
    #     return False


def get_ip() -> str:
    response = requests.get("http://icanhazip.com/")
    return response.content.decode()
