import base64

import requests

import natas7
from helpers import between


def hex2bin(s: str) -> str:
    return bytes.fromhex(s).decode("utf-8")


def strrev(s: str) -> str:
    return s[::-1]


def base64_decode(s: str) -> str:
    return base64.b64decode(s)


def solution() -> str:
    url = "http://natas8.natas.labs.overthewire.org"
    username = "natas8"
    password = natas7.solution()

    # From "View sourcecode" link:
    # $encodedSecret = "3d3d516343746d4d6d6c315669563362";
    #
    # function encodeSecret($secret) {
    #     return bin2hex(strrev(base64_encode($secret)));
    # }

    encoded_secret = "3d3d516343746d4d6d6c315669563362"
    secret = base64_decode(strrev(hex2bin(encoded_secret)))
    data = {"secret": secret, "submit": "Submit+Query"}
    r = requests.post(url, auth=(username, password), data=data)
    start = "The password for natas9 is "
    end = "\n<form method=post>"
    natas9_password = between(r.text, start, end)
    return natas9_password
