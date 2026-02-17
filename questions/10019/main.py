import sys

data = sys.stdin.read().split()

num_of_nums = data[0]

for i in range(1, len(data)):
    target = data[i]
    hex = int(target, 16)

    hex_binary = bin(hex)[2:]
    binary = bin(int(target))[2:]
    b_1 = 0
    b_2 = 0
    for j in binary:
        b_1 += int(j)
    for k in hex_binary:
        b_2 += int(k)

    print(f"{b_1} {b_2}")
    
    
