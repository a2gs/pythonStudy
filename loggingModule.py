#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

def func():
	logging.debug('This is a debug message')
	logging.info('This is an info message')
	logging.warning('This is a warning message')
	logging.error('This is an error message')
	logging.critical('This is a critical message')

	try:
		c = 1 / 0
	except Exception as e:
		logging.exception("Exception occurred", exc_info=True) #exc_info to on/off this log

logging.basicConfig(filename='log.text', filemode='a', level=logging.DEBUG, format='%(asctime)s %(msecs)d - %(process)d - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)d - %(message)s', datefmt='%Y%m%d %H%M%S')
func()
logging.shutdown()

# Log rotation:
# logging.basicConfig(
# 	handlers=[RotatingFileHandler('./my_log.log', maxBytes=200000, backupCount=2)],
# 	level=logging.DEBUG,
# 	format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
# 	datefmt='%Y-%m-%dT%H:%M:%S')
