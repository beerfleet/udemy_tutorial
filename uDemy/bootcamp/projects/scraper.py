import requests
import bs4
import csv


class Scraper():
    def __init__(self, url, page):
        self.url = url
        self.page = page
        self.path = f"{url}/{page}"


if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
