groceries = {}

while True:
    try:
        item = input().upper()
        try:
            groceries[item] += 1
        except KeyError:
            groceries[item] = 1
    except EOFError:
        for grocery, qty in sorted(groceries.items()):
            print(f"{qty} {grocery}")
        break