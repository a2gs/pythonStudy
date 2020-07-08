#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# http://www.freeproxylists.net/
proxies = {
	'https' : '36.89.189.11:46946',
	'http' : '36.89.189.11:46946'
}

url = 'http://httpbin.org/ip'

req = requests.get(url, proxies = proxies)

print(req.text)
