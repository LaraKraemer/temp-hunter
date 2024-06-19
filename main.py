import sqlite3
import requests
import selectorlib
from src import creds
from datetime import datetime
import time

date = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
connection = sqlite3.connect("files/data.db")
cursor = connection.cursor()

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """extract temp data"""
    extractor = selectorlib.Extractor.from_yaml_file("files/extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(date, extracted):
    """store date, temp data"""
    date = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temp VALUES(?,?)", (date, extracted))
    connection.commit()


if __name__ == "__main__":
    while True:
        scraped = scrape(creds.URL)
        temperature = extract(scraped)
        store(date, temperature)
    time.sleep(5)

# Close the connection
conection.close()