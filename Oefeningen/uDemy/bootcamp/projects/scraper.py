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
        self.quotes_list = []
        self.random_quote = []
        self.quotes_file_path = "C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/quotes.txt"
        self.columns = ['name', 'text', 'bio']
        self._fetch_quotes()
        self._choose_quote()
        self.nr_of_guesses = 4
        self._display_game_title()

    def _display_game_title(self):
        print('\n\n\n\n')
        print("**********************************")
        print("*       WHO's QUOTE IS THIS      *")
        print("**********************************")


    def _add_quotes_to_list(self, html):
        """From html abstraction, retrieve all quotes class elements
        and add them to the quotes list, in order to easily query
        """
        self.quotes_html = html.select(".quote")
        for q in self.quotes_html:
            self.quotes_list.append([
                q.select(".author")[0].text,
                q.select(".text")[0].text,
                url + q.find("a")['href']
            ])

    def _retrieve_response(self, url):
        """Retrieve the http response from url        
        """
        response = requests.get(url)
        return BeautifulSoup(response.content, "html.parser")

    def _choose_quote(self):
        """Randomly select one of the quotes in the quotes list
        """
        self.random_quote = choice(self.quotes_list)

    def _fetch_quotes(self):
        """Grab all quotes from the website
        """
        html = self._retrieve_response(self.url)
        self._add_quotes_to_list(html)
        next_tag = html.select(".next")
        while next_tag:
            volgende_pagina = next_tag[0].find("a")["href"]
            html = self._retrieve_response(self.url + volgende_pagina)
            self._add_quotes_to_list(html)
            next_tag = html.select(".next")

    def _ask_question(self):
        """Ask question: whos' quote is this ?
        """
        print('Quote: ' + self.random_quote[1] + '\n')
        print(f"Number of guesses left: {self.nr_of_guesses} \n")
        return str.lower(input("Who said it ? "))

    def _hint_helper_retrieve_bio_hint(self, bio_text):
        """From bio_text, extract one random sentence, where the first 
        name and surname of the author is substituted, if necessary.
        Hints are at least 20 characters long.
        """
        names = self.random_quote[0].split(" ")
        lines = bio_text.split(",")        
        selected_line = choice(lines).lower()
        while len(selected_line) < 20:
            selected_line = choice(lines).lower()
        selected_line = selected_line.replace(names[0].lower(), ' XXXXXX ')
        selected_line = selected_line.replace(names[1].lower(), ' YYYYYY ')
        return selected_line

    def _hint_helper(self, guess_nr, selector, out_message):            
        if self.nr_of_guesses == guess_nr:            
            # return quote author's date or place of birth 
            html = self._retrieve_response(self.random_quote[2])
            item = html.select(selector)[0].text
            if guess_nr == 1: # extract info from bio
                bio_hint = self._hint_helper_retrieve_bio_hint(item)
                out_message = f"------------------ \n* HINT {4 - guess_nr}: {out_message} = {bio_hint} *\n------------------\n"
            else:
                out_message = f"------------------ \n* HINT {4 - guess_nr}: {out_message} = {item} *\n------------------\n"
            print(out_message)

    def _hint(self):
        """Give hints after each turn.
        """
        self._hint_helper(3, ".author-born-date", "Date of birth")
        self._hint_helper(2, ".author-born-location", "Place of birth")
        self._hint_helper(1, ".author-description", "Bio hint")

    def play_again(self):
        nog_eens = input("Wanna play again ? : ")
        if nog_eens.lower() in ['ja', 'j', 'y', 'yes']:
            return True
        return False

    def play(self):
        while self.nr_of_guesses > 0:
            answer = self._ask_question()  # acquire answer from user
            if answer == str.lower(self.random_quote[0]):  # correct answer
                print("That is the CORRECT ANSWER, well done ! \n")
                return
            else:  # incorrect answer
                self.nr_of_guesses -= 1
                print("Wrong answer.\n")
                self._hint()  # hints
        print("All guesses used up, you lose !!! \n")


if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    play = True
    while play:        
        scraper = Scraper(url)
        scraper.play()
        play = scraper.play_again()
