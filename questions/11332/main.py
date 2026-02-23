import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    if line == "0":
        break
    current = line
    while len(current) > 1:
        current = str(sum(map(int, current)))
    
    print(current) 

