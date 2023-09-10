import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level > 0:
            break

answer = random.choice(range(1, level + 1))

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < 0:
            pass
        elif guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break