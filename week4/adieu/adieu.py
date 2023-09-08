import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip()
    except EOFError:
        break
    else:
        names.append(name)

print(f"Adieu, adieu, to {p.join(names)}")
