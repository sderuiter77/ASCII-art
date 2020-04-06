from pyfiglet import Figlet
from termcolor import colored
from colorama import init
init()

f = Figlet(font='big')

text = input("What message do you want to print?")
color = input("What color?").lower()

try:
    colored(f.renderText('test'),color=color)
except:
    print("You didn't input a valid color, but we chose magenta for you")
    print(colored(f.renderText(text),color="magenta"))
else: 
    print(colored(f.renderText(text),color=color))
