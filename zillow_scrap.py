import requests
from bs4 import BeautifulSoup


class ZillowScraper:

    def __init__(self):
        zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
        headers = {'user-agent': 'my-app/0.0.1'}

        self.link_list = []
        self.price_list = []
        self.address_list = []

        # Get the page
        self.response = requests.get(url=zillow_clone_url, headers=headers)
        self.homes_html = self.response.text
        self.homes_soup = BeautifulSoup(self.homes_html, "html.parser")

    def scrape_homes(self):
        # Get the list of all homes
        home_listings = self.homes_soup.find_all(class_="StyledPropertyCardDataWrapper")
        print(len(home_listings))
        print(home_listings[0].text)

        self.link_list = [home.find(name="a").attrs["href"] for home in home_listings]
        self.price_list = [home.find(name="span",class_="PropertyCardWrapper__StyledPriceLine").get_text().replace('/mo', '').split("+")[0] for home in home_listings]
        self.address_list = [home.find(name="address").get_text().replace('\n','').replace('|','').strip() for home in home_listings]
        return self.link_list, self.price_list, self.address_list

