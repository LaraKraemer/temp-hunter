import requests
import selectorlib
import time
import creds

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """extract temp data"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


if __name__ == "__main__":
    scraped = scrape(creds.URL)
    extracted = extract(scraped)
    print(extracted)