import requests

from helpers import between


def solution() -> str:
    url = "http://natas0.natas.labs.overthewire.org/"
    username = "natas0"
    password = "natas0"

    r = requests.get(url, auth=(username, password))
    start = "<!--The password for natas1 is "
    end = " -->"
    natas1_password = between(r.text, start, end)
    return natas1_password
