=================================================
REQUIREMENTS:
=================================================
INSTALLED PACKAGES:

[Flask]: Microframework for building complex web application

-- pip install flask
=================================================

[Waitress]: Waitress WSGI server: production-quality pure-Python WSGI server with acceptable performance.

-- pip install waitress
=================================================

[Selenium]: Package is used to automate web browser interaction from Python.

-- pip install selenium
==================================================

Driver: geckodriver (Firefox driver). This is located in driver folder.
==================================================

[Scrapy]: High level web crawling & web scrapy framework

-- pip install Scrapy3

==================================================
[scrapy-xlsx]: Scrapy exporter that supports the XLSX format. produce a file that can be read by Microsoft Excel.

-- pip install scrapy-xlsx

==================================================

app.py: this the flask application runs which listens to user inputs: zip & radius
simple form web page can be accessed via http://localhost:5001/index


The application is organised as follows

app.py : handles user request from a simple web page.

selenium_worker: that handles automation: input of zip & radius

scrapping application: firstscrapper\firstscrapper\spidersedmundsbot_2.py (this can be run manually or invoke automatically from selenium_worker

scrapped data in saved in firstscrapper\edmunds.xlsx 