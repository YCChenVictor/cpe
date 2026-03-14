while True:
    try:
        line = input()
        values = list(map(int, line.split()))
        num_of_nums = values[0]
        targets = [False] * (num_of_nums - 1)
        for i in range(2, len(values)):
            index = abs(values[i] - values[i - 1]) - 1
            if index < len(targets):
                targets[abs(values[i] - values[i - 1]) - 1] = True
        if all(targets):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
