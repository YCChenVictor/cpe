import sys

lines = sys.stdin.read().splitlines()

collection = {}
i = 0
j = 0
while i < len(lines):
    [num_of_rows, num_of_cols] = lines[i].split()
    num_of_rows = int(num_of_rows)
    num_of_cols = int(num_of_cols)
    collection[j] = {}
    collection[j]['nums'] = lines[i]
    i += 1
    if num_of_rows == 0:
        break
    collection[j]['mine'] = lines[i:i+num_of_rows]
    collection[j]['answer'] = [[0]*num_of_cols for _ in range(num_of_rows)]
    i += num_of_rows
    j += 1

dirs = [(-1,-1), (-1,0), (-1,1),
        ( 0,-1),         ( 0,1),
        ( 1,-1), ( 1,0), ( 1,1)]
for k in collection:
    [num_of_rows, num_of_cols] = collection[k]['nums'].split()
    if num_of_rows == '0':
        continue
    mine = collection[k]['mine']
    num_of_rows = int(num_of_rows)
    num_of_cols = int(num_of_cols)
    answer = collection[k]['answer']
    for i in range(0, num_of_rows):
        for j in range(0, num_of_cols):
            if(mine[i][j] == '*'):
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < num_of_rows and 0 <= nj < num_of_cols:
                        answer[ni][nj] += 1
    for i in range(0, num_of_rows):
        for j in range(0, num_of_cols):
            if(mine[i][j] == '*'):
                answer[i][j] = '*'
    collection[k]['answer'] = answer
    print(f"Field #{k + 1}:")
    for row in answer:
        print("".join(map(str, row)))
    print()
