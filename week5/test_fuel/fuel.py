def main():
    fraction = input("Fraction: ")

    percentage = convert(fraction)
    gauge(percentage)


def convert(fraction):
    num, den = fraction.split("/")
    try:
        return int(num) / int(den) * 100
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid fraction")


def gauge(percentage):
    if percentage > 100:
        raise ValueError("Percentage cannot be greater than 100")
    elif percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()
