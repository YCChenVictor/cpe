import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    number = int(line)
    binary_form = format(number, "b")
    ones = sum(map(int, binary_form))
    
    if line == '0':
        print("")
    else:
        print(f"The parity of {binary_form} is {ones} (mod 2).")
