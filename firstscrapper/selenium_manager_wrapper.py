#!/usr/bin/python3.7
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''

from interface import implements

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from selenium_interface_wrapper import SeleniumInterfaceWrapper

class SeleniumManagerWrapper(implements(SeleniumInterfaceWrapper)):

	def set_preference(self,profile_name,path):
		options = Options()
		options.set_preference(profile_name,path)#
		
		return options
		
	def set_service(self,driver_path):
		service = Service(driver_path)
		
		return service
		
	def init_driver(self,service,options):
		my_driver = Firefox(service=service, options=options)
		
		return my_driver