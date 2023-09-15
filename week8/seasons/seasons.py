from datetime import date
import inflect
import sys


def main():
    delta = get_birth_date() - date.today()
    text = convert_to_text(delta).capitalize().replace(" and", "")
    print(f"{text} minutes")


def get_birth_date():
    while True:
        birth = input("Date of Birth: ")
        try:
            return date.fromisoformat(birth)
        except ValueError:
            sys.exit("Invalid date")


def convert_to_text(delta):
    p = inflect.engine()
    minutes = int(-delta.total_seconds() / 60)
    return p.number_to_words(minutes)


if __name__ == "__main__":
    main()
