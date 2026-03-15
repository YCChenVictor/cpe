i = 0
while True:
    try:
        rows, cols = map(int, input().split())
        if (rows == 0 or cols == 0):
            break
        i += 1
        print(f"Field #{i}:")
        matrix = []
        for row in range(rows):
            matrix.append(input())

        dir = [(-1, 1), (0, 1), (1, 1),
               (-1, 0), (0, 0), (1, 0),
               (-1, -1), (0, -1), (1, -1)]
        answer = []
        for row in range(rows):
            ans_row = ""
            for col in range(cols):
                if matrix[row][col] == "*":
                    ans_row += "*"
                else:
                    count = 0
                    for dx, dy in dir:
                        nx = row + dx
                        ny = col + dy
                        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == "*":
                            count += 1
                    ans_row += str(count)
            print(ans_row)
        print("")
    except EOFError:
        break
