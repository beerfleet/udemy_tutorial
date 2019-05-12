import requests
from bs4 import BeautifulSoup
from csv import reader, writer


class Scraper():
    """Scraper class facilitates traversing of html content"""
    def __init__(self, url: str):
        """Initialize Scraper. 
        
        path: url/page        
        html: html elements list from content
        """
        self.url = url
        self.quotes_file_path = "C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/quotes.txt"
        self.quotes_list = []

    def funcname(self, parameter_list):
        pass
    
    def build_quotes_file():
        # fetch all quotes
        pass

if __name__ == "__main__":    
    url = "http://quotes.toscrape.com"
    scraper = Scraper(url)
    scraper.build_quotes_file()
 