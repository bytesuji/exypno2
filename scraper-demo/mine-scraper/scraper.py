import sys
import json
from requests.exceptions import ConnectionError
from WayfairScraper import WayfairScraper

def main():
    try:
        url = sys.argv[1]
    except IndexError:
        print("Usage: scraper <url>")
        exit(-1)

    try:
        scraper = WayfairScraper(url)
    except ConnectionError:
        print("ConnectionError: Invalid URL!");
        exit(0)

    folio = scraper.product_portfolio()
    print(json.dumps(folio))

if __name__ == '__main__':
    main()
