import requests

import natas0
from helpers import between


def solution() -> str:
    url = "http://natas1.natas.labs.overthewire.org"
    username = "natas1"
    password = natas0.solution()

    r = requests.get(url, auth=(username, password))

    # This looks just like natas0, but right click is blocked in the browser.

    start = "<!--The password for natas2 is "
    end = " -->"
    natas2_password = between(r.text, start, end)
    return natas2_password
