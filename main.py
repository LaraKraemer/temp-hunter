import requests
import selectorlib
import creds
from datetime import datetime

output_file = "data.txt"
date = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

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

def store(date, temperature):
    with open(output_file, "a") as file:
        file.write(f"{date}, {temperature}" + "\n")



if __name__ == "__main__":
    scraped = scrape(creds.URL)
    temperature = extract(scraped)
    store(date, temperature )