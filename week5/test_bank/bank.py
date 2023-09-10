def main():
    val = value(input("Greeting: ").strip())
    print(f"${val}")


def is_hello(greeting):
    return "hello" in greeting.lower()


def starts_with_h(greeting):
    return "h" in greeting.lower()[0]


def value(greeting):
    if is_hello(greeting):
        return int(0)
    elif starts_with_h(greeting):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
