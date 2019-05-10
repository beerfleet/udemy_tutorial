import requests
from bs4 import BeautifulSoup
import csv


class Scraper():
    """Scraper class facilitates traversing of html content"""
    def __init__(self, url: str):
        """Initialize Scraper. 
        
        path: url/page        
        html: html elements list from content
        """
        self.url = url            

    def build_quotes_file():

if __name__ == "__main__":    
    url = "http://quotes.toscrape.com"
    scraper = Scraper(url)
    scraper.build_quotes_file()
