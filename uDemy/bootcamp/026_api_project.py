import pyfiglet as pf
import requests as req
from random import choice

def print_ascii_title():
    result = pf.figlet_format("Dad Joke 3000")
    print(result + "\n\n")

def ask_for_input():
    return input("Let me tell you a joke! Give me a topic: ")

def make_request(term):
    url = "https://icanhazdadjoke.com/search"
    result = req.get(
        url, 
        headers={"Accept": "application/json"}, 
        params={"term": term}
    )
    return result.json()
    
def choose_joke(topic):
    result = make_request(topic)
    joke_count = len(result["results"])
    if joke_count > 0:
        joke = choice(result["results"])
        joke_cnt = joke_count if joke_count != 1 else "one"
        print(f"I've got {joke_cnt} '{topic}' jokes up my sleeve")
        print(joke['joke'])
    else:
        print("Alas, there are no jokes ...")

def main():
    topic = ""
    print_ascii_title()
    topic = ask_for_input() 
    choose_joke(topic)
    
main()
