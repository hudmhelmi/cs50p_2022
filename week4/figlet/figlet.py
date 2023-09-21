import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

# Check number of command-line args
if len(sys.argv) not in (1, 3):
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "-fonts"):
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

text = input("Input: ")

if len(sys.argv) == 1:
    # 1 arg, random font
    figlet.setFont(font=random.choice(figlet.getFonts()))
else:  # 3 args, specified font
    figlet.setFont(font=sys.argv[2])

print(f"Output: \n{figlet.renderText(text)}")
