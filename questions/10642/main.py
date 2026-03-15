cases = int(input())


def index(x, y):
    s = x + y
    return (1 + s) * s / 2 + x


for case in range(cases):
    x1, y1, x2, y2 = map(int, input().split())
    
    print(f"Case {case + 1}: {int(index(x2, y2) - index(x1, y1))}")