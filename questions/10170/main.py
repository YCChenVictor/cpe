while True:
    try:
        add, target = map(int, input().split())
        total = 0
        while True:
            total += add
            if total >= target:
                print(add)
                break
            add += 1
        
    except EOFError:
        break