import requests


def add_five(arg: int) -> int:
    return arg + 5


def blubb(arg: bool) -> bool:
    if arg:
        return True
    else:
        return False


def get_ip() -> str:
    response = requests.get("http://icanhazip.com/")
    return response.content.decode()
