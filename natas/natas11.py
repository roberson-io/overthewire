import base64
from urllib.parse import quote, unquote

import requests

import natas10
from helpers import between

"""
From "View sourcecode" link:

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
"""


def show_key() -> str:
    # This shows that the key is just "qw8J" repeating.
    default_data = '{"showpassword":"no","bgcolor":"#ffffff"}'
    cookie_data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D"
    decoded = base64.b64decode(unquote(cookie_data))
    key = "".join(chr(a ^ ord(b)) for a, b in zip(decoded, default_data))
    print(key)


def create_key(length: int) -> str:
    padded_length = length // 4 + 1
    return ("qw8J" * padded_length)[:length]


def xor_encrypt(s: str) -> str:
    key = create_key(len(s))
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, key))


def create_cookie(s: str) -> str:
    return quote(base64.b64encode(xor_encrypt(s).encode("utf-8")))


def solution() -> str:
    url = "http://natas11.natas.labs.overthewire.org"
    username = "natas11"
    password = natas10.solution()

    s = requests.Session()
    payload = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    s.cookies["data"] = create_cookie(payload)
    r = s.get(url, auth=(username, password))
    start = "The password for natas12 is "
    end = "<br>\n<form>"
    return between(r.text, start, end)
