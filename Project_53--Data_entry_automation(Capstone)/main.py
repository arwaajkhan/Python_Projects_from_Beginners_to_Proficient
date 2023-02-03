from using_beautifulsoup import WebScraping
from using_selenium import Selenium

web_scraping_obj = WebScraping()
selenium_obj = Selenium()

price__list = web_scraping_obj.price_list
link__list = web_scraping_obj.link_list
address__list = web_scraping_obj.address_list

for i in range(len(price__list)):
    selenium_obj.filling_into_sheet(link__list[i], price__list[i], address__list[i])

