import sys

lines = sys.stdin.read().splitlines()

case = 1
for i in range(1, len(lines), 3):
    numbers = lines[i].split()
    sums = set()
    is_B2 = True
    stop = False
    for k in range(0, len(numbers)):
        for s in range(k, len(numbers)):
            sum = int(numbers[k]) + int(numbers[s])
            if sum in sums:
                is_B2 = False
                stop = True
                break
            sums.add(sum)
        if stop:
            break
            
    if is_B2:
        print(f"Case #{case}: It is a B2-Sequence.")
    else:
        print(f"Case #{case}: It is not a B2-Sequence.")
    case += 1
    print("")
