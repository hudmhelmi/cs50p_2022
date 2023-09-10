def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    if not s[0:2].isalpha():
        return False
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not 2 <= len(s) <= 6:
        return False
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    for i in range(len(s) - 1):
        first_num = True
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            else:
                first_num = False
        if s[i].isnumeric() and not s[i + 1].isnumeric():
            return False
    # “No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c == "." or c.isspace() or c == "," or c == "!" or c == "?":
            return False

    return True

if __name__ == "__main__":
    main()
