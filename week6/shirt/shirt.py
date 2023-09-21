import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[2].lower())[1] not in (".jpg", ".jpeg", ".png"):
    sys.exit("Invalid output")
elif (
    not os.path.splitext(sys.argv[1].lower())[1]
    == os.path.splitext(sys.argv[2].lower())[1]
):
    sys.exit("Input and output have different extensions")
elif not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist")

try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Include shirt.png in the same directory")

before = Image.open(sys.argv[1])
size = shirt.size
before = ImageOps.fit(before, size)
before.paste(shirt, shirt)
before.save(sys.argv[2])
