import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    [n, m] = line.split()
    n = int(n)
    m = int(m)
    
    if n <= 1  or m == 0 or n < m:
        print(f"Boring!")
        continue
    
    answer = [n]
    while True:
        if n % m == 0:
            answer.append(int(n/m))
        n = n/m
        if n == 1 or n/m >= n:
            break
    
    if len(answer) == 0:
        print(f"Boring!")
    elif answer[len(answer) - 1] == 1:
        print(f"{' '.join(map(str, answer))}")
    else:
        print(f"Boring!")
