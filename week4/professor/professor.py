import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        tries = 0
        X = generate_integer(level)
        Y = generate_integer(level)
        while tries < 3:
            try:
                answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                pass
            else:
                if answer == X + Y:
                    score += 1
                    break
                elif answer != X + Y and tries < 2:
                    print("EEE")
                    tries += 1
                else:
                    print("EEE")
                    tries += 1
                    print(f"{X} + {Y} = {X + Y}")
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in (1, 2, 3):
                return level



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()
