def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print()


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / float(60)


if __name__ == "__main__":
    main()
