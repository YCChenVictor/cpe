while True:
    try:
        n = int(input())
        print(n + n // 2)
        # just think multiple 2s
    except EOFError:
        break