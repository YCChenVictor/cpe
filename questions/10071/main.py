while True:
    try:
        line = input()
        v, t = map(int, line.split())
        print(v * 2 * t)
    except EOFError:
        break