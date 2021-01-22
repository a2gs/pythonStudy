#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

keyPB        = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
userNamePB   = 'bbbb'
userPasswdPB = 'cccccccccccccccc'
textPB       = 'Test 1234567890 abcdefghijlmnopqrstuvxz'
titlePB      = 'Test Title'

loginData = {
	'api_dev_key'       : keyPB,
	'api_user_name'     : userNamePB,
	'api_user_password' : userPasswdPB
}

data = {
	'api_option'            : 'paste',
	'api_dev_key'           : keyPB,
	'api_paste_code'        : textPB,
	'api_paste_name'        : titlePB,
	'api_paste_expire_date' : '10M',
	'api_user_key'          : None,
	#'api_paste_format'     : '',
	'api_paste_private'     : '2' # public = 0, unlisted = 1, private = 2
}

loginRetPB = requests.post("https://pastebin.com/api/api_login.php", data = loginData)
print(f"Login status: [{loginRetPB.status_code}]")

if loginRetPB.status_code != 200:
	print(f"Error login: [{loginRetPB.text}]")
	exit(1)

print(f"User token: [{loginRetPB.text}]")

data['api_user_key'] = loginRetPB.text

postRetPB = requests.post("https://pastebin.com/api/api_post.php", data = data)
print(f"Paste status: [{postRetPB.status_code}]")

if postRetPB.status_code != 200:
	print(f"Error pasting: [{postRetPB.text}]")
	exit(1)

print(f"Paste URL: [{postRetPB.text}]")

'''
# Public (not member) PasteBin

dataPubPB = {
	'api_option': 'paste',
	'api_dev_key': keyPB,
	'api_paste_code': textPB,
	'api_paste_name': titlePB,
	'api_paste_expire_date': '10M',
	'api_user_key': None,
	#'api_paste_format': '',
	'api_paste_private' : '0' # public = 0, unlisted = 1, private = 2
}

postPubRetPB = requests.post("https://pastebin.com/api/api_post.php", data = dataPubPB)
print(f"Paste status: [{postPubRetPB.status_code}]")

if postPubRetPB.status_code != 200:
	print(f"Error pasting: [{postPubRetPB.text}]")
	exit(1)

print(f"Paste URL: [{postPubRetPB.text}]")
'''