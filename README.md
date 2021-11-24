# UnicodeToy
Unicode fuzzer for various purposes
> Unicode based on version 14.0

# features
- Generate the shortest xss domain payload
- Generate unicode str, use NFKC mechanism to bypass some filter: python3, rust...(N-CTF 2019 python_jail)
- ...


# usage
- `toy.py` main tool
- `script/get_latest_TLDs.py` grab latest TLD from IANA
- `script/get_latest_unicode.py` grab latest unicode collection from unicode.org (version 14.0.0)

# ref
- https://xz.aliyun.com/t/9271
- https://pockr.org/guest/activity?activity_no=act_017d460d4e5988dad2&speech_no=sp_940aedc9e73b0a79a6
- https://www.tr0y.wang/2020/08/18/IDN/#%E5%88%A9%E7%94%A8%E5%9C%BA%E6%99%AF