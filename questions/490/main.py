import sys

lines = sys.stdin.read().splitlines()

max_len = 0
for line in lines:
    if len(line) > max_len:
        max_len = len(line)

for i in range(max_len):
    current_answer = ""
    for line in lines:
        if i > len(line) - 1:
            current_answer = ' ' + current_answer
        else:
            current_answer = line[i] + current_answer
    print(current_answer)
