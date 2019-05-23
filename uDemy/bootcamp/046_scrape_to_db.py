from projects.mysqlhelper import MySqlHelper
from bs4 import BeautifulSoup, Tag
import requests
import pymysql

class Grabber():
  def __init__(self, base_url):
    self.base_url = base_url
    self.next_page = '/'
  
  def next_page_exists(self):
    return self.next_page != ''

  def grab_books(self, path=''):
    if path:
        response = requests.get(f"{self.base_url}{path}")
    else:
        response = requests.get(self.base_url)
    bs = BeautifulSoup(response.content, "html.parser")
    self.next_page = bs.select('.next a')[0]["href"]
    if 'catalogue' not in self.next_page:
      self.next_page.replace('/page', '/catalogue/page')
    return bs.find_all('article', {'class': 'product_pod'})

  def translate_rating(self, rating):
    return {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}[rating]

  def strip_chars(self, string, chars):
    return string.replace(chars, '')

  def store_in_bulk(self, args):
    my_helper = MySqlHelper('localhost', 'root', '', 'pydb')
    sql = "INSERT INTO books (title, rating, price) VALUES (%s, %s, %s)"
    my_helper.execute_in_bulk(sql, args)

  def build_dataset(self, path=''):
    books = self.grab_books(path)
    book_list = []
    for book in books:
      title = book.find("h3").find("a")["title"]
      rating = self.translate_rating(book.find("p")["class"][1])
      price = self.strip_chars(book.select("div .price_color")[0].get_text(), '£')
      book_list.append((title, rating, price))
    return book_list

  def execute(self):
    while self.next_page:
      data_set = self.build_dataset(self.next_page)
      self.store_in_bulk(data_set)


if __name__ == "__main__":
  grab = Grabber('http://books.toscrape.com/')
  grab.execute()
  