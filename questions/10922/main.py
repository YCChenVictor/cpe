import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    if line == '0':
        continue

    number = line
    total = sum(map(int, number))
    if total % 9 != 0:
        print(f'{line} is not a multiple of 9.')
        break    
    
    degree = 0
    while True:
        total = sum(map(int, number))
        degree += 1
        if total == 9:
            print(f'{line} is a multiple of 9 and has 9-degree {degree}.')
            break
        number = str(total)
