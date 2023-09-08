s = input("Input: ")
final = ""
for c in s:
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
print(f"Output: {final}")
