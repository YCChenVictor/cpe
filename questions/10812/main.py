t = int(input())

for _ in range(t):
    # x + y = sum
    # x - y = diff
    # x > y
    # x = (sum + diff) / 2
    # y = (sum - diff) / 2
    sum, diff = map(int, input().split())
    x = (sum + diff) / 2
    y = (sum - diff) / 2
    if (not x.is_integer()) or (not y.is_integer()) or (x < 0) or (y < 0):
        print("impossible")
    else:
        print(int(x), int(y))
