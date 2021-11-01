#!/usr/bin/python3.7
'''
author: alex_irungu
technical interview: Dviz: edmunds.
run in script in supervisord
'''

import os
import sys

from scrapy import cmdline

def run_scrapy_command():
	
	cmdline.execute("scrapy crawl edmundsbot_2".split())
	
if(__name__=='__main__'):
	try:
		run_scrapy_command()
	except KeyboardInterrupt:
		exit()