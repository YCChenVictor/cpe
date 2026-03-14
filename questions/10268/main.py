while True:
    try:
        x = int(input())
        params = list(map(int, input().split()))
        length = len(params)
        dev_params = []
        for i in range(length):
            dev_params.append((length - i - 1) * params[i])
        if x == 0:
            print(int(dev_params[len(dev_params) - 2]))
            continue
        answer = 0
        power = 0
        for i in range(length - 1, -1, -1):
            answer += x ** (power - 1) * dev_params[i]
            power += 1
        print(int(answer))
    except EOFError:
        break
