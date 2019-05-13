import requests
from bs4 import BeautifulSoup
from csv import reader, writer
from random import choice


class Scraper():
    """Scraper class facilitates traversing of html content"""

    def __init__(self, url: str):
        """Initialize Scraper.         
        """
        self.url = url
        self.quotes_file_path = "C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/quotes.txt"
        self.quotes_list = []
        self.columns = ['name', 'text', 'bio']
        self._fetch_quotes()
        self._choose_quote()
        self.nr_of_guesses = 4

    def _add_quotes_to_dict(self, html):
        self.quotes_html = html.select(".quote")
        for q in self.quotes_html:
            self.quotes_list.append([
                q.select(".author")[0].text,
                q.select(".text")[0].text,
                url + q.find("a")['href']
            ])

    def _retrieve_response(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.content, "html.parser")

    def _choose_quote(self):
        self.random_quote = choice(self.quotes_list)

    def _fetch_quotes(self):
        html = self._retrieve_response(self.url)
        self._add_quotes_to_dict(html)
        next_tag = html.select(".next")
        while next_tag:
            volgende_pagina = next_tag[0].find("a")["href"]
            html = self._retrieve_response(self.url + volgende_pagina)
            self._add_quotes_to_dict(html)
            next_tag = html.select(".next")

    def _ask_question(self):
        print(" ************  ")
        print(self.random_quote[1] + '\n')
        print(f"Number of guesses left: {self.nr_of_guesses} \n")
        return str.lower(input("Who said it ? "))

    def _hint1(self):
        if self.nr_of_guesses == 3:
            # return quote author's date of borth
            return

    def play(self):
        while self.nr_of_guesses > 0:
            answer = self._ask_question()
            self._hint1()  # hint after first guess
            if answer == str.lower(self.random_quote[0]):
                print("That is the correct answer, well done ! \n")
                return
            else:
                print("Wrong answer, try again. \n")
                self.nr_of_guesses -= 1
        print("All guesses used up, you lose !!! \n")


if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    scraper = Scraper(url)
    scraper.play()
