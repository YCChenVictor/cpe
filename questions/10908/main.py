cases = int(input())

for case in range(cases):
    rows, columns, centers = map(int, input().split())

    matrix = []
    for row in range(rows):
        matrix.append(input())

    for center in range(centers):
        r, c = map(int, input().split())
        ch = matrix[r][c]

        answer = 1  ## init is it self
        k = 1
        while True:
            top = r - k
            bottom = r + k
            left = c - k
            right = c + k

            if top < 0 or left < 0 or bottom > (rows - 1) or right > (columns - 1):
                break

            extract_matrix = []
            ok = True
            for i in range(top, bottom):
                for j in range(left, right):
                    if matrix[i][j] != ch:
                        ok = False
                        break 
                if not ok:
                    break
            if not ok:
                break

            answer = k * 2 + 1
            k += 1

        print(answer)
