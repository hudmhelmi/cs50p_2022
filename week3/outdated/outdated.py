def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        mdy = input("Date: ")

        # split
        if "/" in mdy:
            try:
                year, month, day = parse_num_dates(mdy)
            except TypeError:
                print("TypeError")
        elif "," in mdy:
            try:
                year, month, day = parse_full_dates(mdy, months)
            except TypeError:
                pass
        else:
            pass

        # validate
        try:
            if month > 12 or day > 31:
                pass
            else:
                break
        except UnboundLocalError:
            pass

    print(f"{year:04}-{month:02}-{day:02}")


def parse_num_dates(mdy):
    month, day, year = mdy.split("/")
    try:
        return int(year), int(month), int(day)
    except ValueError:
        return False


def parse_full_dates(mdy, months):
    # Remove comma
    mdy = mdy.replace(",", "")
    month, day, year = mdy.split(" ")
    try:
        month = months.index(month) + 1  # + 1 because index starts at 0
    except ValueError:
        return False
    return int(year), int(month), int(day)


if __name__ == "__main__":
    main()
