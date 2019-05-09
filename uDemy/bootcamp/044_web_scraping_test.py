import requests
from bs4 import BeautifulSoup
from csv import reader, writer


def retrieve_page_content(url):
    response = requests.get(url)
    #return response.text   # returns string
    return response.content   # returns byte object


def seek_elements(content, selector="div"):
    selectable_content = BeautifulSoup(content, "html.parser")
    return selectable_content.select(selector)


def write_to_file(content):
    pad = "C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/scrape.txt"
    with open(pad, mode='w', encoding='utf8', newline='') as scrape_file:
        html_writer = writer(scrape_file)
        html_writer.writerows(content)


if __name__ == "__main__":
    url = "https://www.rithmschool.com/blog"
    response_content = retrieve_page_content(url)
    content = seek_elements(response_content)
    write_to_file(content)
