#!/usr/bin/python3
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''

import os

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium_manager_wrapper import SeleniumManagerWrapper
from cache.MemcacheWrapper import MemcacheWrapper
from cache.MemcacheConnection import MemcacheConnection

#from dotenv import load_dotenv

class SeleniumWorker():
	
	def worker_manager(self,user_input):
	
		TARGET_URL = 'https://www.edmunds.com/cars-for-sale-by-owner/'
		
		selenium_manager = SeleniumManagerWrapper()
		'''
		set option
		'''
		options = selenium_manager.set_preference('profile',r'profile\firefox.default')
		'''
		init the service via Firefox drive.
		'''
		service = selenium_manager.set_service(r'drivers\geckodriver.exe')
		'''
		init drive.
		'''
		my_driver = selenium_manager.init_driver(service,options)
		'''
		pass website url.
		'''
		my_driver.get(TARGET_URL)	
		'''
		invoke a delay.
		'''		
		my_driver.implicitly_wait(20)
		'''
		automate: enter zip input.
		'''
		zip_search = my_driver.find_element(By.NAME, 'zip')
		zip_search.send_keys(user_input[0]) 
		zip_search.send_keys(Keys.RETURN)
		'''
		invoke a delay.
		'''
		my_driver.implicitly_wait(20)
		'''
		automate slider input: //-TODO: this piece of code does not work as expected.
		'''
		radius = lambda:my_driver.find_element(By.XPATH ,"//*[@id='search-radius-range-min']")
	
		'''
		move = ActionChains(my_driver)
		
		move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
		my_driver.implicitly_wait(20)
		move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
		my_driver.implicitly_wait(20)
		move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
		my_driver.implicitly_wait(20)
		'''
		
		'''
		automate anchor click()
		'''
		anchor = my_driver.find_element(By.XPATH ,"//html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/ul/li[1]/div/div[2]/div/h2/a[@class='usurp-inventory-card-vdp-link']")
		my_driver.execute_script("arguments[0].scrollIntoView();", anchor)
		my_driver.execute_script("arguments[0].click();", anchor)
		'''
		get the url of the target page.
		'''
		wait = WebDriverWait(my_driver, 50)
		wait.until(EC.title_contains('- VIN:'))
		
		target_url = my_driver.current_url
		'''
		1st part of url after split at ? point. https://www.edmunds.com/chevrolet/silverado-1500/2012/vin/3GCPKTE7XCG146177/?radius=xxx
		'''
		leading_url = target_url.split('?')[0]
		'''
		2nd part: override the radius value with user input.
		'''
		query_part = '?radius=' + str(user_input[1])
		
		new_url = leading_url + query_part
		
		print(new_url)
		'''
		store the new url in cache.
		'''
		memcache_connection = MemcacheConnection()
		client = memcache_connection.create_client_connection('127.0.0.1')
		memcache_wrapper = MemcacheWrapper(client)
		memcache_wrapper.set_input_value('NEW_URL',new_url)
		'''
		cmdline.execute("scrapy crawl edmundsbot_2".split())
		'''