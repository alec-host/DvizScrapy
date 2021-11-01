#!/usr/bin/python3.7
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''

import redis

from interface import implements

from .memcache_interface_connection import MemcacheInterfaceConnection

class MemcacheConnection(implements(MemcacheInterfaceConnection)):

	def create_client_connection(self,host):
	
		client = redis.Redis(host=host,port=6379,db=0)
		
		return client
