import math

while True:
    try:
        line = input()
        if line == "0 0":
            break
        start, end = map(int, line.split())
        s_root = start ** 0.5
        e_root = end ** 0.5
        print(math.floor(e_root) - math.ceil(s_root) + 1)
    except EOFError:
        break
