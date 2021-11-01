'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''

import scrapy

from cache.MemcacheWrapper import MemcacheWrapper
from cache.MemcacheConnection import MemcacheConnection

class Edmundsbot2Spider(scrapy.Spider):

	name = 'edmundsbot_2'
	allowed_domains = ['www.edmunds.com']
	'''
	store the new url in cache.
	'''
	memcache_connection = MemcacheConnection()
	client = memcache_connection.create_client_connection('127.0.0.1')
	memcache_wrapper = MemcacheWrapper(client)
	url = memcache_wrapper.get_input_value('NEW_URL')
	'''
	read the url from the generated new_url
	'''
	if(url == '' or url is None):
		url = 'https://www.edmunds.com/ford/f-150/2019/vin/1FTEW1E47KKE59930/?radius=200'
	else:
		url = url.decode("utf-8")
	
	'''
	clear all keys.
	'''
	memcache_wrapper.flush_cache()
		
	start_urls = [str(url)]
	
	def parse(self, response):
		#-.name element.
		vehicle_name = response.xpath('//h1/text()').extract()
		#-.price element.
		price = response.xpath('//html/body/div[1]/div/main/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/span/text()').extract()
		#-.vin element.
		vin = response.xpath('//section/div[2]/div/span[1]/text()[2]').extract()
		#-.section: vehicle_summary.
		vehicle_summary_divs = response.xpath('//div[@class="mb-0 max-width text-capitalize pl-1_25 pl-md-0 pl-lg-1_25 row"]')
		for div in vehicle_summary_divs:
			vehicle_summary = [
				div.xpath('//div[@class="col"]/text()').extract_first(),
				div.xpath('//div[@class="col"]/span/text()').extract_first(),
				div.xpath('//div[@class="col"]/span/text()').extract()[1],
				div.xpath('//div[@class="col"]/text()').extract()[1],
				div.xpath('//div[@class="col"]/text()').extract()[2],
				div.xpath('//div[@class="col"]/text()').extract()[3],
				div.xpath('//div[@class="col"]/text()').extract()[4],
				div.xpath('//div[@class="col"]/text()').extract()[5],
				div.xpath('//div[@class="col"]/text()').extract()[6]
			]
			
		#-.section: top feature & specs.
		top_feature_specs_sub_topics = response.xpath('//div[@class="font-weight-bold mb-0_5"]/text()').extract()

		if(int(len(top_feature_specs_sub_topics)) > 1):
			ul = response.xpath('//ul[@class="pl-1 mb-0"]')
			for li in ul:
				top_feature_spec = [
					str(top_feature_specs_sub_topics[1]) +" : "+
					li.xpath('//li[@class="mb-0_5"]/text()').extract_first(),
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[1],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[2],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[3],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[4],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[5],
					str(top_feature_specs_sub_topics[2]) +" : "+
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[6],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[7],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[8],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[9],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[10],
					str(top_feature_specs_sub_topics[3]) +" : "+
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[11],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[12],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[13],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[14],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[15],
					str(top_feature_specs_sub_topics[4]) +" : "+
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[16],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[17],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[18],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[19],
					li.xpath('//li[@class="mb-0_5"]/text()').extract()[20]
				]
		else:
			top_feature_spec = [None, None]

		for item in zip(vehicle_name,price,vin,vehicle_summary,top_feature_spec):
			#-.create a dictionary.
			scrapped_vehicle_info = {
				'Name' : item[0],
				'Price' : item[1],
				'VIN Number' : item[2],
				'Vehicle Summary' : vehicle_summary,
				'Top Features & Specs' :  top_feature_spec
			}
		
		yield scrapped_vehicle_info