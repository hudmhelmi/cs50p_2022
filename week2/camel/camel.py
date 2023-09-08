camel = input("camelCase: ")
snake = ""
for char in camel:
    if char.islower():
        snake = snake + char
    else:
        snake = snake + f"_{char.lower()}"
print(f"snake_case: {snake}")
