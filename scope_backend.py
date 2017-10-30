# Attempts to run post requests to addresses given in the template code
# and returns ones that don't 404.

import requests

base = "http://10.66.28.202:"
urls = [
    "/"
    "/waf/detect/test",
    "/waf/email/test",
    "/waf/password/test",
    "/waf/custom/field=5%20test=5",
    "/waf/debug",
    "/api/useradd/user/pass",
    "/api/userget/user",
    "/api/userget/all",
    "/detect/test",
    "/email/test",
    "/password/test",
    "/custom/field=5%20test=5",
    "/debug",
    "/useradd/user/pass",
    "/userget/user",
    "/userget/all"
]

ports = [
    8076,
    8156,
    8157,
    8201,
    8202,
    8236,
    8237,
    8231,
]

for port in ports:
    for url in urls:
        r = requests.post("{base}{port}{url}".format(base=base, port=str(port),
            url=url))
        if r.status_code != 404:
            print(port, url, r.status_code)

