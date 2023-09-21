while True:
    fraction = input("Fraction: ")

    try:
        num, den = fraction.split("/")
        percentage = (int(num) / int(den)) * 100
    except (ValueError, ZeroDivisionError):
        continue
    else:
        if percentage > 100:
            pass
        elif percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage:.0f}%")
            break
