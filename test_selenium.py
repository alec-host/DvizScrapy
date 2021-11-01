#!/usr/bin/python3
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''
import os
import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from scrapy import cmdline

#from dotenv import load_dotenv
	
def worker_manager():

	options=Options()
	
	options.set_preference('profile',r'profile\firefox.default')
	
	service = Service(r'drivers\geckodriver.exe')
	
	my_driver = Firefox(service=service, options=options)
	
	my_driver.get('https://www.edmunds.com/cars-for-sale-by-owner/')
	
	my_driver.implicitly_wait(20)
	'''
	automate: enter search input.
	'''
	zip_search = my_driver.find_element(By.NAME, 'zip')
	zip_search.send_keys('68067') 
	zip_search.send_keys(Keys.RETURN)
	my_driver.implicitly_wait(20)
	
	radius = lambda:my_driver.find_element(By.XPATH ,"//*[@id='search-radius-range-min']")
	
	#slider().send_keys(Keys.ENTER)
	#my_driver.execute_script("arguments[0].scrollIntoView();", anchor)

	
	move = ActionChains(my_driver)
	
	move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
	my_driver.implicitly_wait(25)
	move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
	my_driver.implicitly_wait(25)
	move.click_and_hold(radius()).move_by_offset(-90,0).release().perform()
	my_driver.implicitly_wait(25)

	move = ActionChains(my_driver)
	anchor = my_driver.find_element(By.XPATH ,"//html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/ul/li[1]/div/div[2]/div/h2/a[@class='usurp-inventory-card-vdp-link']")
	#print(anchor)
	#anchor.click()
	#anchor.send_keys("\n")
	#move.move_to_element(anchor).perform()
	#wait = WebDriverWait(my_driver, 2000000)
	
	#wait.until(EC.invisibility_of_element_located(By.XPATH("//html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/ul/li[1]/div/div[2]/div/h2/a[@class='usurp-inventory-card-vdp-link']"))).click()
	
	#wait.until(EC.element_to_be_clickable((By.XPATH, "//html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/ul/li[1]/div/div[2]/div/h2/a[@class='usurp-inventory-card-vdp-link']"))).click()
	
	my_driver.execute_script("arguments[0].scrollIntoView();", anchor)
	my_driver.execute_script("arguments[0].click();", anchor)
	
	
	wait = WebDriverWait(my_driver, 10)
	wait.until(EC.title_contains('- VIN:'))
	
	target_url = my_driver.current_url
	
	print(target_url)
	
	'''
	try:
		cards = WebDriverWait(my_driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "d-flex flex-column usurp-inventory-card rounded w-100")))
	finally:
		my_driver.close()
    '''
	'''
	for x in range(0,len(card)):
		if card[x].is_displayed():
			card[x].click()
	'''
	
	'''
	automate: button  click go to initiate search. (not reliable as the button disappears)
	'''
	#my_driver.find_element_by_xpath("//button[@class='px-0_5 py-0_5 zip-button text-transform-none btn btn-success']").click()
	
	"""
	workers = []
	'''
	initiate rabbit mq connection.
	'''
	rabbit_mq = RabbitMQConnection()
	'''
	initiate rabbit mq wrapper.
	'''
	rabbit_mq_wrapper = RabbitMQWrapper("ipn_paypal_queue","ipn_exchange","fanout")
	'''
	connect & return channel.
	'''
	channel = rabbit_mq.create_connection("localhost")
	'''
	define queue.
	'''	
	rabbit_mq_wrapper.define_mq_queue(channel)
	
	t1 = threading.Thread(target=rabbit_mq_wrapper.consumer,args=(channel,))
	t1.daemon = True
	workers.append(t1)
	t1.start()
	
	time.sleep(50)
	
	
	
	for t in workers:
		t.join()
	"""
	#time.sleep(500)
	#my_driver.quit()
if __name__ == '__main__':
	try:
		worker_manager()
	except(KeyboardInterrupt,SystemExit):
		print('Mananger: done sleeping; time to stop the threads')
		exit(0)