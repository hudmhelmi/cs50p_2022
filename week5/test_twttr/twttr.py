def main():
    s = input("Input: ")
    print(f"Output: {shorten(s)}")


def shorten(word):
    final = ""
    for c in word:
        if (
            c == "A"
            or c == "a"
            or c == "E"
            or c == "e"
            or c == "I"
            or c == "i"
            or c == "O"
            or c == "o"
            or c == "U"
            or c == "u"
        ):
            pass
        else:
            final = final + c
    return final


if __name__ == "__main__":
    main()
