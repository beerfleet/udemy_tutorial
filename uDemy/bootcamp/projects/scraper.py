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
        self.quotes_dict = {}

    def fetch_quotes(self):
        response = requests.get(self.url)
        html = BeautifulSoup(response.content, "html.parser")
        self.quotes_list = html.select(".quote")
        self.quotes_dict = {
            'name': html.select(".quote .author")[0].text,
            'text': html.select(".quote .text")[0].text,
            'bio': html.select(".quote").find()
            }
        next_tag = html.select(".next")
        while next_tag:
            volgende_pagina = next_tag[0].find("a")["href"]            
            response = requests.get(self.url + volgende_pagina)
            html = BeautifulSoup(response.content, "html.parser")
            self.quotes_list.extend(html.select(".quote"))
            next_tag = html.select(".next")    

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    scraper = Scraper(url)
    scraper.fetch_quotes()    
