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

    def fetch_quotes_list(self):
        response = requests.get(self.url)
        html = BeautifulSoup(response.content, "html.parser")
        self.quotes_list = html.select(".quote")
        next_tag = html.select(".next")
        while next_tag:
            volgende_pagina = next_tag[0].find("a")["href"]            
            response = requests.get(self.url + volgende_pagina)
            html = BeautifulSoup(response.content, "html.parser")
            self.quotes_list.extend(html.select(".quote"))
            next_tag = html.select(".next")        

    def build_quotes_file(self):
        with open(self.quotes_file_path, mode="w", encoding='utf8', newline='') as quotes_file:
            quotes_csv = writer(quotes_file)
            quotes_csv.writerows(self.quotes_list)

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    scraper = Scraper(url)
    scraper.fetch_quotes_list()
    scraper.build_quotes_file()
