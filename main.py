from zillow_scrap import ZillowScraper
from googleFormFiller import googleFormFiller



zillow_scraper = ZillowScraper()
link_list, price_list, addr_list = zillow_scraper.scrape_homes()

google_form_filler = googleFormFiller(link_list, price_list, addr_list)
google_form_filler.fillForm()
google_form_filler.show_sheet()



