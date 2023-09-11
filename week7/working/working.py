import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Converts 12h time, e.g.,
    "9:00 AM to 5:00 PM" or
    "9 AM to 5 PM"
    to "09:00 to 17:00".
    """

    # Use regex to capture start and end time
    pattern = r"(\d\d?)\:?(\d?\d?) ((?:A|P)M) to (\d\d?)\:?(\d?\d?) ((?:A|P)M)"
    match = re.search(pattern, s)
    if not match:
        raise ValueError
    start_hour = int(match[1])
    try:
        start_min = int(match[2])
    except ValueError:
        start_min = 0
    start_ampm = match[3]
    end_hour = int(match[4])
    try:
        end_min = int(match[5])
    except ValueError:
        end_min = 0
    end_ampm = match[6]

    if start_hour > 12 or end_hour > 12:
        raise ValueError

    if end_hour > 59 or end_min > 59:
        raise ValueError

    if start_hour == 12 and start_ampm == "AM":
        start_hour = 0
    if end_hour == 12 and end_ampm == "AM":
        end_hour = 0
    if start_hour != 12 and start_ampm == "PM":
        start_hour = (start_hour + 12) % 24
    if end_hour != 12 and end_ampm == "PM":
        end_hour = (end_hour + 12) % 24

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


if __name__ == "__main__":
    main()
