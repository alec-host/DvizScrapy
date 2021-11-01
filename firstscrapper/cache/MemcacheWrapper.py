#!/usr/bin/python3.7
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''

from interface import implements

from .memcache_interface_wrapper import MemcacheInterfaceWrapper

class MemcacheWrapper(implements(MemcacheInterfaceWrapper)):
	
	def __init__(self, client):
		self.client = client
		
	def set_input_value(self,key,value):
	    self.client.set(key,value)
		
	def get_input_value(self,key):
		stored_value = self.client.get(key)
		return stored_value
		
	def flush_cache(self):
		self.client.flushall()