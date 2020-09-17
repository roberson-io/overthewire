import requests

import natas27
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return ""
    url = "http://natas28.natas.labs.overthewire.org"
    username = "natas28"
    if not password:
        password = natas27.solution(cheat=True)

    # No source code this time.

    auth = (username, password)