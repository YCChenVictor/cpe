while True:
    try:
        number = int(input())
        if number == 0:
            continue
        if number % 11 == 0:
            print(f"{number} is a multiple of 11.")
        else:
            print(f"{number} is not a multiple of 11.")
    except EOFError:
        break
