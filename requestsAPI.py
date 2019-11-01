#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import requests

validUrl = 'https://api.github.com'
invalidUrl1 = 'https://api.github.com/not_found'
invalidUrl2 = 'https://abcdefg321.com/'

print('---1----------------------')

try:
	validUrlResponse = requests.get(validUrl)
except:
	print(f'Error/exception requesting \'{validUrl}\': {validUrl}')
else:
	print(f'GET response to \'{validUrl}\': {validUrlResponse.status_code}')

print('---2----------------------')
try:
	invalidUrlResponse1 = requests.get(invalidUrl1)
except:
	print(f'Error/exception requesting \'{invalidUrl1}\': {invalidUrlResponse1}')
else:
	print(f'GET response to \'{invalidUrl1}\': {invalidUrlResponse1.status_code}')

print('---3----------------------')

try:
	invalidUrlResponse2 = requests.get(invalidUrl2)
except requests.exceptions.ConnectionError as err:
	print(f'Error/exception requesting \'{invalidUrl2}\': {err}') # invalidUrlResponse2 is undefined
except:
	print(f'Error/exception requesting \'{invalidUrl2}\': {invalidUrlResponse2.status_code}')
else:
	print(f'GET response to \'{invalidUrl2}\': {invalidUrlResponse2.status_code}')

print('---4----------------------')
if len(sys.argv) == 2:
	userUrl = sys.argv[1]

	print(f'Testing GET to {userUrl}:')

	try:
		userUrlResponse = requests.get(userUrl)
	except requests.exceptions.HTTPError as err:
		print(f'An HTTP error occurred: {err}')

	except requests.exceptions.ConnectionError as err:
		print(f'A Connection error occurred: {err}')

	except requests.exceptions.ProxyError as err:
		print(f'A proxy error occurred: {err}')

	except requests.exceptions.SSLError as err:
		print(f'An SSL error occurred: {err}')

	except requests.exceptions.Timeout as err:
		print(f'The request timed out: {err}')

	except requests.exceptions.ConnectTimeout as err:
		print(f'The request timed out while trying to connect to the remote server. Requests that produced this error are safe to retry: {err}')

	except requests.exceptions.ReadTimeout as err:
		print(f'The server did not send any data in the allotted amount of time: {err}')

	except requests.exceptions.URLRequired as err:
		print(f'A valid URL is required to make a request: {err}')

	except requests.exceptions.TooManyRedirects as err:
		print(f'Too many redirects: {err}')

	except requests.exceptions.MissingSchema as err:
		print(f'The URL schema (e.g. http or https) is missing: {err}')

	except requests.exceptions.InvalidSchema as err:
		print(f'See defaults.py for valid schemas: {err}')

	except requests.exceptions.InvalidURL as err:
		print(f'The URL provided was somehow invalid: {err}')

	except requests.exceptions.InvalidHeader as err:
		print(f'The header value provided was somehow invalid: {err}')

	except requests.exceptions.InvalidProxyURL as err:
		print(f'The proxy URL provided is invalid: {err}')

	except requests.exceptions.ChunkedEncodingError as err:
		print(f'The server declared chunked encoding but sent an invalid chunk: {err}')

	except requests.exceptions.ContentDecodingError as err:
		print(f'Failed to decode response content: {err}')

	except requests.exceptions.StreamConsumedError as err:
		print(f'The content for this response was already consumed: {err}')

	except requests.exceptions.RetryError as err:
		print(f'Custom retries logic failed: {err}')

	except requests.exceptions.UnrewindableBodyError as err:
		print(f'Requests encountered an error when trying to rewind a body: {err}')

	except requests.exceptions.RequestsWarning as err:
		print(f'Base warning for Requests: {err}')

	except requests.exceptions.FileModeWarning as err:
		print(f'A file was opened in text mode, but Requests determined its binary length: {err}')

	except requests.exceptions.RequestsDependencyWarning as err:
		print(f'An imported dependency doesnt match the expected version range: {err}')

	else:
		print(f'GET response to \'{userUrl}\': {userUrlResponse.status_code}')

else:
	print(f'No parameter to {sys.argv[0]} defined. Use \'{sys.argv[0]} [URL]\' to test.')
