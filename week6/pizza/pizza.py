import csv
from tabulate import tabulate
import sys


def main():
    # Check if the user has provided the correct number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Get the name of the CSV file
    csv_filename = sys.argv[1] if len(sys.argv) == 2 else None

    # Check if the CSV file exists
    if not csv_filename:
        sys.exit("File does not exist")
    if not csv_filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Open the CSV file
    with open(csv_filename) as csv_file:
        reader = csv.DictReader(csv_file)

        # Create a table of the pizza data
        table = []
        for row in reader:
            table.append(row)

        # Print the table in ASCII art format
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
