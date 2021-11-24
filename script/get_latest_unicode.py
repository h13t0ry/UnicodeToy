# -*- coding: utf-8 -*-
import requests


def grab_unicode_set():
    content = ""
    try:
        resp = requests.get("https://www.unicode.org/Public/14.0.0/ucd/UnicodeData.txt", timeout=10, verify=True)
        content = resp.text
    except requests.RequestException as e:
        print("request error:" + str(e))
        exit(-1)

    lines = content.split("\n")
    lines = [line for line in lines if line]
    unicode_list = map(
        lambda x: f"0x{x.split(';')[0]}", lines
    )

    with open("../data/unicodes.txt", "w") as f:
        f.writelines([unicode + '\n' for unicode in unicode_list])


if __name__ == '__main__':
    grab_unicode_set()
