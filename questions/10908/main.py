import sys

lines = sys.stdin.read().splitlines()

retangles = {}
i = 0
cases = lines[0]
i += 1
while i < len(lines):
    print(lines[i])
    [num_of_row, num_of_col, examples] = lines[i].split()
    num_of_row = int(num_of_row)
    num_of_col = int(num_of_col)
    examples = int(examples)
    
    i += 1
     
    retangle = []
    for j in range(i, i + num_of_row):
        row = lines[j]
        row = list(row)
        retangle.append(row)

    i += num_of_row

    central = []
    for k in range(i, i + examples):
        central.append(lines[k])

    i += examples
   
    for center in central:
        x, y = map(int, center.split())   # x=row, y=col
        should_be = retangle[x][y]

        answer = 1
        k = 0

        while True:
            k += 1
            left   = y - k
            right  = y + k
            top    = x - k
            bottom = x + k

            # out of bounds => stop
            if left < 0 or top < 0 or right >= num_of_col or bottom >= num_of_row:
                break

            ok = True

            # check top & bottom rows
            for col in range(left, right + 1):
                if retangle[top][col] != should_be or retangle[bottom][col] != should_be:
                    ok = False
                    break

            # check left & right columns (skip corners)
            if ok:
                for row in range(top + 1, bottom):
                    if retangle[row][left] != should_be or retangle[row][right] != should_be:
                        ok = False
                        break

            if not ok:
                break

            answer += 2   # 1->3->5...

        print(answer) 
