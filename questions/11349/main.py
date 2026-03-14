# rotate 180 degrees
# 11 -> 33 (44)
# 12 -> 32 (44)
# 13 -> 31 (44)
# 21 -> 23 (44)
# 23 -> 21
# 31 -> 13

def check(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            if matrix[i][j] < 0:
                return False
            if matrix[i][j] != matrix[len(matrix) - i - 1][len(matrix) - j - 1]:
                return False
    return True
                

cases = input()
current_case = 1
while True:
    try:
        size = int(input().split()[-1])
        matrix = []
        for _ in range(size):
            matrix.append(list(map(int, input().split())))
        if check(matrix):
            print(f"Test #{current_case}: Symmetric.")
        else:
            print(f"Test #{current_case}: Non-symmetric.")
        current_case += 1
    except EOFError:
        break
