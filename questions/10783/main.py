import sys

lines = sys.stdin.read().splitlines()

examples = lines[0]
case = 1
for i in range(1, len(lines), 2):
    start = int(lines[i])
    if start % 2 == 0:
        start += 1
    end = int(lines[i+1])
    if end % 2 == 0:
        end -= 1
    
    height = (end - start) / 2 + 1
    answer = (start + end) * height / 2

    print(f"Case {case}: {int(answer)}")
    case += 1
