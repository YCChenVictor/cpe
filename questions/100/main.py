while True:
    try:
        a, b = map(int, input().split())
        start = min(a, b)
        end = max(a, b)
        answer = 0
        for i in range(start, end + 1):
            n = i
            count = 1
            while (n != 1):
                if (n % 2 == 1):
                    n = 3 * n + 1
                else:
                    n = n / 2
                count += 1
            if count > answer:
                answer = count
        print(a, b, answer)
    except EOFError:
        break