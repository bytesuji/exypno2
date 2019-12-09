import re
import requests
from bs4 import BeautifulSoup

class WayfairScraper(object):
    def _validate_url(self, url):
        wayfair = re.compile("wayfair.com")
        pdp = re.compile("/pdp/") # product display page, presumably
        if not (wayfair.search(url) and pdp.search(url)):
            return False
        return True

    def _page_has_captcha(self, soup):
        ## returns None if page has no captcha
        captcha = re.compile("Captcha-title")
        return captcha.search(soup.title.get_text())

    def __init__(self, url):
        if not self._validate_url(url):
            raise requests.exceptions.ConnectionError(
                "Connection error: {} is not a valid Wayfair product URL.".format(url))

        self.url = url

        ## collect the page at `url` and put it into a soup.
        agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
        headers = {'User-Agent': agent}

        self.document = requests.get(url, headers=headers).text
        self.soup = BeautifulSoup(self.document, 'lxml')
        if self._page_has_captcha(self.soup):
            raise Exception("CAPTCHA detected, try updating the agent string.")

        ## extract title, price, product images, and description
        try:
            self.title = self.soup.h1.get_text() # make more robust
        except AttributeError:
            raise requests.exceptions.ConnectionError(
                "Connection error: {} is not a valid Wayfair product URL.".format(url))
            
        price_div = self.soup.find("div", {"class": "BasePriceBlock"})
        self.price = price_div.find("span").get_text()

        self.description = self.soup.find("div",
            {"class": "ProductOverviewInformation-description"}).get_text()

        media_div = self.soup.find("div", {"class": "ProductDetailSingleMediaItem"})
        self.image = media_div.find("img")['src']

    def product_portfolio(self):
        portfolio = {
            "title": self.title,
            "image": self.image,
            "price": self.price,
            "desc": self.description
        }

        return portfolio

## TODO
## - randomize User-Agent string to avoid detection
## - more robust image collection (list of links)
## - get images for multiple finishes / colors / options
