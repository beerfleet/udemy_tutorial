import pyfiglet as pyf
import random
from termcolor import colored
# help(termcolor)

# text = termcolor.colored(text="Hi there",  color="red",  on_color="on_yellow",  attrs=['blink', 'reverse'])
# print(text)

#help(pyf.figlet_format)

msg = "Print this message"
color = random.choice(['red', 'yellow',  'teal',  'blue'])
ascii_art = pyf.figlet_format(msg)
colored_ascii = colored(ascii_art,  color='yellow')
print(colored_ascii)
