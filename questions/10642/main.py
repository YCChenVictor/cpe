import sys

lines = sys.stdin.read().splitlines()

def index(x, y):
    s = x + y
    return s * (s+1) / 2 + x

num_of_ex = int(lines[0])
for i in range(1, len(lines)):
    [x_1, y_1, x_2, y_2] = lines[i].split()
    index_1 = index(int(x_1), int(y_1))
    index_2 = index(int(x_2), int(y_2))

    print(f"Case {i}: {int(index_2 - index_1)}")
    

