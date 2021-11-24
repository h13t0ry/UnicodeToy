# -*- coding: utf-8 -*-
import requests
import hashlib
import idna


def grab_TLDs():
    content = ""
    try:
        resp = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt", timeout=10, verify=True)
        md5_resp = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt.md5", timeout=10, verify=True)
        content = resp.text
        md5_content = md5_resp.text
        content_md5 = hashlib.md5(content.encode()).hexdigest()
        if content_md5 in md5_content:
            print("get TLDs success, md5 match！")
        else:
            print("get TLDs success, md5 don't match！")
        return content
    except requests.RequestException as e:
        print("request error:" + str(e))
        exit(-1)

    TLDs = content.split("\n")
    valid_TLDs = list(
        map(
            lambda x: idna.decode(x.strip()),
            filter(
                lambda x: x and not x.startswith("#"), TLDs
            )
        )
    )

    with open("../data/TLDs.txt", "w") as f:
        f.writelines([line+'\n' for line in valid_TLDs])


if __name__ == '__main__':
    grab_TLDs()
