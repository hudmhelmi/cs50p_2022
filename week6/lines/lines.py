import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        num_lines = count_lines(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(num_lines)


def count_lines(filename):
    with open(filename) as file:
        lines = file.readlines()

    num_lines = 0
    for line in lines:
        if not line.lstrip().startswith("#") and not line.isspace():
            num_lines += 1

    return num_lines


if __name__ == "__main__":
    main()
