#!/usr/local/bin/python3
# coding: utf-8

# WebsiteRunner - cfip.py
# 4/9/21 20:47
#

__author__ = "Benny <benny.think@gmail.com>"

import requests

v4 = requests.get("https://www.cloudflare.com/ips-v4").text
v6 = requests.get("https://www.cloudflare.com/ips-v6").text
config = ""

for item in v4.split():
    directive = f"set_real_ip_from {item};\n"
    config += directive
config += "\n"
for item in v6.split():
    directive = f"set_real_ip_from {item};\n"
    config += directive

bottom = "real_ip_header CF-Connecting-IP;"
config += "\n" + bottom

with open("cloudflare.conf", "w")as f:
    f.write(config)
