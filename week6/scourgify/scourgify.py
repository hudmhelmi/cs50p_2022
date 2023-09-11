import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)

            with open(output_filename, "w") as output_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
