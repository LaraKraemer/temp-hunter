import requests
import selectorlib
import time
import creds

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

if __name__ == "__main__":
    scraped = scrape(creds.URL)
    print(scraped)