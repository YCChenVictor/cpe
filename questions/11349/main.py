import sys

lines = sys.stdin.read().splitlines()

def check(matrix):
    length = len(matrix)
    for m in range(0, length):
        for n in range(0, length):
            if int(matrix[m][n]) < 0:
                return False
            mm, nn = length - 1 - m, length - 1 - n
            if (m, n) <= (mm, nn):
                if int(matrix[m][n]) != int(matrix[mm][nn]):
                    return False
    return True

i = 0
i += 1
case = 1
while i < len(lines):
    matrix_size = int(lines[i].replace("N = ", ""))
    i += 1
    matrix = []
    for j in range(i, i+matrix_size):
        matrix.append(lines[j].split())
    i += matrix_size

    if check(matrix):
        print(f"Test #{case}: Symmetric.")
    else:
        print(f"Test #{case}: Non-symmetric.")
    case += 1
